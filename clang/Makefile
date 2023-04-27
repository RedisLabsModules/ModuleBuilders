CLANG_VER ?= 16
override OSNICK ?= bullseye

ROOT=..

include $(ROOT)/deps/readies/mk/main

include $(MK)/osnick.defs

ARCH=x64

IMAGE=redisfab/clang:$(CLANG_VER)-$(ARCH)-$(OSNICK)
VIEW=/w

build:
	docker build -t $(IMAGE) --build-arg CLANG_VER=$(CLANG_VER) --build-arg OSNICK=$(OSNICK) --build-arg OS=$(OS) .

publish:
	docker push $(IMAGE)

run:
	docker run -it $(IMAGE) -v $(VIEW):$(VIEW) --cap-add SYS_PTRACE bash
