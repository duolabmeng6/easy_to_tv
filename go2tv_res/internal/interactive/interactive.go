package interactive

import (
	"fmt"
	"github.com/alexballas/go2tv/soapcalls"
	"github.com/gdamore/tcell/v2"
	"os"
	"strconv"
	"sync"
)

// NewScreen .
type NewScreen struct {
	mu         sync.RWMutex
	TV         *soapcalls.TVPayload
	mediaTitle string
	lastAction string
}

var flipflop bool = true

// InterInit starts the interactive terminal
func (p *NewScreen) InterInit(tv *soapcalls.TVPayload) {
	p.TV = tv
	//由于我们需要正确初始化 tcell 窗口，因此更早发送 Play1 操作可能会导致恐慌错误。
	if err := tv.SendtoTV("Play1"); err != nil {
		fmt.Fprintf(os.Stderr, "%v\n", err)
		os.Exit(1)
	}
	服务器启动 := make(chan struct{})
	<-服务器启动

}

// HandleKeyEvent Method to handle all key press events
func (p *NewScreen) HandleKeyEvent(ev *tcell.EventKey) {
	tv := p.TV

	if ev.Key() == tcell.KeyEscape {
		tv.SendtoTV("Stop")
		p.Fini()
	}

	if ev.Key() == tcell.KeyPgUp || ev.Key() == tcell.KeyPgDn {
		currentVolume, err := tv.GetVolumeSoapCall()
		if err != nil {
			return
		}

		setVolume := currentVolume - 1
		if ev.Key() == tcell.KeyPgUp {
			setVolume = currentVolume + 1
		}

		stringVolume := strconv.Itoa(setVolume)

		if err := tv.SetVolumeSoapCall(stringVolume); err != nil {
			return
		}
	}

	switch ev.Rune() {
	case 'p':
		if flipflop {
			flipflop = false
			tv.SendtoTV("Pause")
			break
		}

		flipflop = true
		tv.SendtoTV("Play")

	case 'm':
		currentMute, err := tv.GetMuteSoapCall()
		if err != nil {
			break
		}
		switch currentMute {
		case "1":
			if err = tv.SetMuteSoapCall("0"); err == nil {
			}
		case "0":
			if err = tv.SetMuteSoapCall("1"); err == nil {
			}
		}
	}
}

// Fini Method to implement the screen interface
func (p *NewScreen) Fini() {
	os.Exit(0)
}

// InitTcellNewScreen .
func InitTcellNewScreen() (*NewScreen, error) {
	return &NewScreen{}, nil
}

func (p *NewScreen) getLastAction() string {
	p.mu.RLock()
	defer p.mu.RUnlock()
	return p.lastAction
}

func (p *NewScreen) updateLastAction(s string) {
	p.mu.Lock()
	defer p.mu.Unlock()
	p.lastAction = s
}
