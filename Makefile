all: build push

build:
	docker build -t redislabsmodules/rmbuilder .
.PHONY: build

push: build
	docker push redislabsmodules/rmbuilder:latest

