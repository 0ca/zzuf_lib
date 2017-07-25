# How To compile and use it:
You need to use Python 2.7 libraries to compile it. Python 3.X won't work without modifying the C++ code.

## Linux 

```
sudo apt-get install python2.7-dev
git clone https://github.com/0ca/zzuf_windows_lib
cd zzuf_windows_lib
./bootstrap
./configure [CFLAGS=-m32 CXXFLAGS=-m32 LDFLAGS=-m32] for 32bits in 64bits
make
```
Note: Maybe in the future we need to modify the path of the python includes in `src/Makefile.am`. Currently is: `-I/usr/include/python2.7/` Other option is using `CFLAGS=-I/path/python2.7/`.
Note2: For 32bits in a 64 bits OS you need to install the 32bits packages of libc, python and python-dev:
```
sudo apt-get install libc6-dev-i386 python:i386 python-dev:i386
```

Library `libzzuf.so` will be at `src/.libs`

The .so it's a python module. Since it isn't installed it needs to be in the same path of the python script using it.

To test it:
```
cd src/.libs/
cp ../../libfuzz_test.py .
python libfuzz_test.py
```

Expected output:
```
python libfuzz_test.py 
Input: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Output: !aaaaaaaaaaAaaaaaaaaaaa!aaaaaaaaaaaaaaaaaaaaaaaaaa�a!aaaeiaaaaaaaaaaaaaaaaaaaaaacaaaaaaaaaaaaaaaaaaaaacaaaaa`aaaaaaaaaaaaaaaaiaaaaaaaaaaacaaaaaaaaaaaaaaaaaaaaaaaaaaeaAaeaaaqaeaa�aAcaaaaiaaaaaaaaaaaaaa
```

## CentOs 32 bits
First we need a dockerfile for centos 7 32 bits. We can have it following these steps:
https://github.com/nunofernandes/docker-centos7-32bits

I needed to modify one of the steps:
```
- docker export  centos7-32-run | tar xv tmp/centos7*bz2
+ docker export  centos7-32-run | tar xv --wildcards tmp/centos7*bz2
```
Then run /bin/bash in the instance and install dependencies:
```
yum install python-devel.i686 git automake libtool.i686 make
```

After that follow generic steps for linux.

## Windows
Use the Visual Studio project present in `msvc`.

Select Release (If you select debug, the compiler couldn't find Python27_d.lib). And add your Python includes directory to the C++ configuration and the Python27.lib to the linker configuration.

Python bindings reference: https://en.wikibooks.org/wiki/Python_Programming/Extending_with_C

# zzuf_windows_lib
A zzuf library version compiled in windows, plus a python wrapper:


# Original readme
 About zzuf:

zzuf is a transparent application input fuzzer. It works by intercepting
file operations and changing random bits in the program's input. zzuf's
behaviour is deterministic, making it easy to reproduce bugs.

For instructions and examples on how to use zzuf, see the manual page
and the website at <http://caca.zoy.org/wiki/zzuf>.

[![Build Status](https://travis-ci.org/samhocevar/zzuf.svg?branch=master)](https://travis-ci.org/samhocevar/zzuf)
