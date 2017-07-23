import libzzuf
input = "a" * 200
print "Input: %s" % input
seed = 0 # A value from -0x7FFFFFE to 0x7FFFFFFF
ratio = 0.01 # A value from 0 to 1, read zzuf documentation
output = libzzuf.fuzz_buffer(seed, ratio, input)
print "Output: %s" % output
