LDFLAGS="-s -w"

build: clean
	go build -ldflags $(LDFLAGS) -o build/go2tv cmd/go2tv-lite/go2tv.go

install:
	go build -ldflags $(LDFLAGS) -o build/go2tv cmd/go2tv-lite/go2tv.go
	mkdir -vp /usr/local/bin/
	#cp build/go2tv /usr/local/bin/
	cp build/go2tv /Users/chensuilong/Desktop/pythonproject/easy_to_tv


uninstall:
	rm -vf /usr/local/bin/go2tv

clean:
	rm -rf ./build
