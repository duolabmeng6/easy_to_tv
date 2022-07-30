package main

import (
	"context"
	_ "embed"
	"flag"
	"fmt"
	"io"
	"net/url"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
	"sort"
	"strings"
	"sync"
	"time"

	"github.com/alexballas/go2tv/devices"
	"github.com/alexballas/go2tv/httphandlers"
	"github.com/alexballas/go2tv/soapcalls"
	"github.com/alexballas/go2tv/utils"
	"github.com/pkg/errors"
)

var (
	//go:embed version.txt
	version     string
	errNoflag   = errors.New("没有使用标志")
	视频音频文件的本地路径 = flag.String("v", "", "视频音频文件的本地路径。 （触发 CLI 模式）")
	媒体文件的       = flag.String("u", "", "媒体文件的 HTTP URL。 URL 流不支持查找操作。 （触发 CLI 模式）")
	字幕文件的本地路径   = flag.String("s", "", "字幕文件的本地路径。")
	目标URL       = flag.String("t", "", "投射到特定的 UPnP DLNA 媒体渲染器 URL。")
	文件转码路径      = flag.Bool("tc", false, "使用 ffmpeg 对输入视频文件进行转码。")
	所有设备列表      = flag.Bool("l", false, "列出所有可用的 UPnPDLNA 媒体渲染器模型和 URL。")

	版本号 = flag.Bool("version", false, "版本号。")
)

type flagResults struct {
	dmrURL string
	exit   bool
}

func main() {
	var absMediaFile string
	var mediaType string
	var 媒体文件 interface{}
	var isSeek bool

	flag.Parse()

	flagRes, err := processflags()
	check(err)

	if flagRes.exit {
		os.Exit(0)
	}

	if *视频音频文件的本地路径 != "" {
		媒体文件 = *视频音频文件的本地路径
	}

	if *视频音频文件的本地路径 == "" && *媒体文件的 != "" {
		mediaURL, err := utils.StreamURL(context.Background(), *媒体文件的)
		check(err)

		mediaURLinfo, err := utils.StreamURL(context.Background(), *媒体文件的)
		check(err)

		mediaType, err = utils.GetMimeDetailsFromStream(mediaURLinfo)
		check(err)

		媒体文件 = mediaURL

		if strings.Contains(mediaType, "image") {
			readerToBytes, err := io.ReadAll(mediaURL)
			mediaURL.Close()
			check(err)
			媒体文件 = readerToBytes
		}
	}

	switch t := 媒体文件.(type) {
	case string:
		absMediaFile, err = filepath.Abs(t)
		check(err)

		mfile, err := os.Open(absMediaFile)
		check(err)

		媒体文件 = absMediaFile
		mediaType, err = utils.GetMimeDetailsFromFile(mfile)

		if !*文件转码路径 {
			isSeek = true
		}

		check(err)
	case io.ReadCloser, []byte:
		absMediaFile = *媒体文件的
	}

	字幕文件, err := filepath.Abs(*字幕文件的本地路径)
	check(err)

	upnpServicesURLs, err := soapcalls.DMRextractor(flagRes.dmrURL)
	check(err)

	whereToListen, err := utils.URLtoListenIPandPort(flagRes.dmrURL)
	check(err)

	//scr, err := interactive.InitTcellNewScreen()
	//check(err)

	callbackPath, err := utils.RandomString()
	check(err)

	tvdata := &soapcalls.TVPayload{
		ControlURL:                  upnpServicesURLs.AvtransportControlURL,
		EventURL:                    upnpServicesURLs.AvtransportEventSubURL,
		RenderingControlURL:         upnpServicesURLs.RenderingControlURL,
		CallbackURL:                 "http://" + whereToListen + "/" + callbackPath,
		MediaURL:                    "http://" + whereToListen + "/" + utils.ConvertFilename(absMediaFile),
		SubtitlesURL:                "http://" + whereToListen + "/" + utils.ConvertFilename(字幕文件),
		MediaType:                   mediaType,
		CurrentTimers:               make(map[string]*time.Timer),
		MediaRenderersStates:        make(map[string]*soapcalls.States),
		InitialMediaRenderersStates: make(map[string]bool),
		RWMutex:                     &sync.RWMutex{},
		Transcode:                   *文件转码路径,
		Seekable:                    isSeek,
	}

	s := httphandlers.NewServer(whereToListen)
	服务器启动 := make(chan struct{})

	//我们在这里传递 tvdata，因为我们需要回调处理程序能够对不同的媒体渲染器状态做出反应。
	go func() {
		err := s.StartServer(服务器启动, 媒体文件, 字幕文件, tvdata)
		check(err)
	}()
	// 等待HTTP服务器正确初始化
	<-服务器启动
	if err := tvdata.SendtoTV("Play1"); err != nil {
		fmt.Fprintf(os.Stderr, "%v\n", err)
		os.Exit(1)
	}
	<-服务器启动
}

func check(err error) {
	if errors.Is(err, errNoflag) {
		flag.Usage()
		os.Exit(0)
	}

	if err != nil {
		_, _ = fmt.Fprintf(os.Stderr, "Encountered error(s): %s\n", err)
		os.Exit(1)
	}
}

func listFlagFunction() error {
	flagsEnabled := 0
	flag.Visit(func(f *flag.Flag) {
		flagsEnabled++
	})

	if flagsEnabled > 1 {
		return errors.New("cant combine -l with other flags")
	}

	deviceList, err := devices.LoadSSDPservices(1)
	if err != nil {
		return errors.New("failed to list devices")
	}

	fmt.Println()

	// We loop through this map twice as we need to maintain
	// the correct order.
	keys := make([]string, 0)
	for k := range deviceList {
		keys = append(keys, k)
	}

	sort.Strings(keys)

	for q, k := range keys {
		boldStart := ""
		boldEnd := ""

		if runtime.GOOS == "linux" {
			boldStart = "\033[1m"
			boldEnd = "\033[0m"
		}
		fmt.Printf("%sDevice %v%s\n", boldStart, q+1, boldEnd)
		fmt.Printf("%s--------%s\n", boldStart, boldEnd)
		fmt.Printf("%sModel:%s %s\n", boldStart, boldEnd, k)
		fmt.Printf("%sURL:%s   %s\n", boldStart, boldEnd, deviceList[k])
		fmt.Println()
	}

	return nil
}

func processflags() (*flagResults, error) {
	checkVerflag()

	res := &flagResults{}

	if *视频音频文件的本地路径 == "" && !*所有设备列表 && *媒体文件的 == "" {
		return nil, fmt.Errorf("checkflags error: %w", errNoflag)
	}

	if err := checkTCflag(res); err != nil {
		return nil, fmt.Errorf("checkflags error: %w", err)
	}

	if err := checkTflag(res); err != nil {
		return nil, fmt.Errorf("checkflags error: %w", err)
	}

	list, err := checkLflag()
	if err != nil {
		return nil, fmt.Errorf("checkflags error: %w", err)
	}

	if list {
		res.exit = true
		return res, nil
	}

	if err := checkVflag(); err != nil {
		return nil, fmt.Errorf("checkflags error: %w", err)
	}

	if err := checkSflag(); err != nil {
		return nil, fmt.Errorf("checkflags error: %w", err)
	}

	return res, nil
}

func checkVflag() error {
	if !*所有设备列表 && *媒体文件的 == "" {
		if _, err := os.Stat(*视频音频文件的本地路径); os.IsNotExist(err) {
			return fmt.Errorf("checkVflags error: %w", err)
		}
	}

	return nil
}

func checkSflag() error {
	if *字幕文件的本地路径 != "" {
		if _, err := os.Stat(*字幕文件的本地路径); os.IsNotExist(err) {
			return fmt.Errorf("checkSflags error: %w", err)
		}
		return nil
	}

	// The checkVflag should happen before checkSflag so we're safe to call
	// *视频音频文件的本地路径 here. If *字幕文件的本地路径 is empty, try to automatically find the
	// srt from the media file filename.
	*字幕文件的本地路径 = (*视频音频文件的本地路径)[0:len(*视频音频文件的本地路径)-
		len(filepath.Ext(*视频音频文件的本地路径))] + ".srt"

	return nil
}

func checkTCflag(res *flagResults) error {
	if *文件转码路径 {
		_, err := exec.LookPath("ffmpeg")
		if err != nil {
			return fmt.Errorf("checkTCflag parse error: %w", err)
		}
	}

	return nil
}

func checkTflag(res *flagResults) error {
	if *目标URL != "" {
		// Validate URL before proceeding.
		_, err := url.ParseRequestURI(*目标URL)
		if err != nil {
			return fmt.Errorf("checkTflag parse error: %w", err)
		}

		res.dmrURL = *目标URL
		return nil
	}

	deviceList, err := devices.LoadSSDPservices(1)
	if err != nil {
		return fmt.Errorf("checkTflag service loading error: %w", err)
	}

	res.dmrURL, err = devices.DevicePicker(deviceList, 1)
	if err != nil {
		return fmt.Errorf("checkTflag device picker error: %w", err)
	}

	return nil
}

func checkLflag() (bool, error) {
	if *所有设备列表 {
		if err := listFlagFunction(); err != nil {
			return false, fmt.Errorf("checkLflag error: %w", err)
		}
		return true, nil
	}

	return false, nil
}

func checkVerflag() {
	if *版本号 && os.Args[1] == "-version" {
		fmt.Printf("Go2TV Version: %s\n", version)
		os.Exit(0)
	}
}
