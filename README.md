# Linux library HOWTO

```
git clone https://github.com/0ca/zzuf_windows_lib
cd zzuf_windows_lib
./bootstrap
./configure [CFLAGS=-m32 CXXFLAGS=-m32 LDFLAGS=-m32] for 32bits in 64bits
make
```
Note: Maybe in the future we need to modify the path of the python includes in `src/Makefile.am`. Currently is: `-I/usr/include/python2.7/`

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

