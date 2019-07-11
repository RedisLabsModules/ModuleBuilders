
all: build push

build:
	docker build -t redislabsmodules/rmbuilder:stretch .
	docker tag redislabsmodules/rmbuilder:latest redislabsmodules/rmbuilder:stretch .
	docker build -t redislabsmodules/rmbuilder:centos7 -f Dockerfile.centos .

publish push: build
	docker push redislabsmodules/rmbuilder:latest
	docker push redislabsmodules/rmbuilder:stretch
	docker push redislabsmodules/rmbuilder:centos7

.PHONY: build push publish
