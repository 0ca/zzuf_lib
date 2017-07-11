import libzzuf
input = "a" * 200
print "Input: %s" % input
seed = 0 # A value from 0 to MAX_INT
ratio = 0.01 # A value from 0 to 1, read zzuf documentation
output = libzzuf.fuzz_buffer(seed, ratio, input, len(input))
print "Output: %s" % output
