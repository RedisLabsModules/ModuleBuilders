# BUILD redisfab/clang:${CLANG_VER}-${ARCH}-${OSNICK}

ARG OSNICK=bullseye
ARG CLANG_VER=13
ARG NINJA_VER=1.10.1
ARG REDIS_VER=6

#----------------------------------------------------------------------------------------------
FROM debian:$OSNICK

ARG OSNICK
ARG CLANG_VER
ARG CMAKE_VER
ARG NINJA_VER
ARG REDIS_VER

WORKDIR /build
SHELL ["/bin/bash", "-c"]

#----------------------------------------------------------------------------------------------
# Install prerequisites

RUN apt-get -qq update
RUN apt-get install -y ca-certificates curl wget
RUN apt-get install -y software-properties-common apt-transport-https
RUN apt-get install -y git unzip lsb-release gnupg2 wget

RUN git clone https://github.com/RedisLabsModules/readies.git

RUN ./readies/bin/getpy3
RUN ./readies/bin/getcmake --usr

# install ninja
RUN set -e ;\
    cd /tmp ;\
    wget -q https://github.com/ninja-build/ninja/releases/download/v${NINJA_VER}/ninja-linux.zip ;\
    unzip ninja-linux.zip ;\
    mv ninja /usr/local/bin/ninja

#----------------------------------------------------------------------------------------------
# Install Clang

RUN set -e ;\
    wget -q https://apt.llvm.org/llvm.sh ;\
    chmod +x llvm.sh ;\
    ./llvm.sh $CLANG_VER
RUN apt-get install -y clang-tools-$CLANG_VER

#----------------------------------------------------------------------------------------------
# Build C++ runtime libs with msan instrumentation

# arrange llvm-* and clang-* version-neutral symlinks
RUN set -e ;\
    cd /usr/bin ;\
    for f in llvm*-$CLANG_VER clang*-$CLANG_VER; do ln -sf $f ${f/%-$CLANG_VER/}; done

# build llvm for msan into /opt/llvm-project/build-msan
RUN set -e ;\
    cd /opt ;\
    git clone --depth=1 https://github.com/llvm/llvm-project ;\
    cd llvm-project ;\
    mkdir build-msan ;\
    cd build-msan ;\
    cmake -GNinja ../llvm \
        -DCMAKE_BUILD_TYPE=Release \
        -DLLVM_ENABLE_PROJECTS="libcxx;libcxxabi" \
        -DCMAKE_C_COMPILER=clang \
        -DCMAKE_CXX_COMPILER=clang++ \
        -DLLVM_USE_SANITIZER=MemoryWithOrigins ;\
    cmake --build . -- cxx cxxabi

#----------------------------------------------------------------------------------------------
# Build Redis with asan/msan instrumentation

ADD redis.blacklist /build/

# build sanitizer-enabled redis-server(s)
# `--no-run` because Clang sanitizer requires SYS_PTRACE docker capability, which is not available in docker build
RUN set -e ;\
    for redis_ver in 6.0 6.2; do \
        ./readies/bin/getredis --no-run -v $redis_ver --suffix asan-${redis_ver} --own-openssl --clang-asan --clang-san-blacklist /build/redis.blacklist ;\
        ./readies/bin/getredis --no-run -v $redis_ver --suffix msan-${redis_ver} --own-openssl --clang-msan --llvm-dir /opt/llvm-project/build-msan --clang-san-blacklist /build/redis.blacklist ;\
    done
