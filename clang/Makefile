
CLANG_VER ?= 12
OSNICK=strech
ARCH=x64
REDIS_VER=6

IMAGE=redisfab/clang:$(CLANG_VER)-$(ARCH)-$(OSNICK)
ifneq ($(REDIS_VER),6)
IMAGE=redisfab/clang:$(CLANG_VER)-$(ARCH)-$(OSNICK)-$(REDIS_VER)
endif
VIEW=/w

build:
	docker build -t $(IMAGE) --build-arg CLANG_VER=$(CLANG_VER) --build-arg REDIS_VER=$(REDIS_VER) .

publish:
	docker push $(IMAGE)

run:
	docker run -it $(IMAGE) -v $(VIEW):$(VIEW) --cap-add SYS_PTRACE bash
