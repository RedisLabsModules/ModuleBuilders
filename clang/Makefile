
CLANG_VER ?= 13
OSNICK ?= bullseye
ARCH=x64
REDIS_VER=6

IMAGE=redisfab/clang:$(CLANG_VER)-$(ARCH)-$(OSNICK)
ifneq ($(REDIS_VER),6)
IMAGE=redisfab/clang:$(CLANG_VER)-$(ARCH)-$(OSNICK)-$(REDIS_VER)
endif
VIEW=/w

build:
	docker build -t $(IMAGE) --build-arg CLANG_VER=$(CLANG_VER) --build-arg OSNICK=$(OSNICK) --build-arg REDIS_VER=$(REDIS_VER) .

publish:
	docker push $(IMAGE)

run:
	docker run -it $(IMAGE) -v $(VIEW):$(VIEW) --cap-add SYS_PTRACE bash
