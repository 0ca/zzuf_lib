# Linux library HOWTO

```
git clone https://github.com/0ca/zzuf_windows_lib
cd zzuf_windows_lib
./bootstrap
./configure [CFLAGS=-m32 CXXFLAGS=-m32 LDFLAGS=-m32] for 32bits in 64bits
./make
```
Library `libzzuf.so` will be at `src/.libs`

# zzuf_windows_lib
A zzuf library version compiled in windows, plus a python wrapper:
https://git.soma.salesforce.com/foca/zzuf_windows_lib/tree/master/msvc/Debug


# Original readme
 About zzuf:

zzuf is a transparent application input fuzzer. It works by intercepting
file operations and changing random bits in the program's input. zzuf's
behaviour is deterministic, making it easy to reproduce bugs.

For instructions and examples on how to use zzuf, see the manual page
and the website at <http://caca.zoy.org/wiki/zzuf>.

[![Build Status](https://travis-ci.org/samhocevar/zzuf.svg?branch=master)](https://travis-ci.org/samhocevar/zzuf)

