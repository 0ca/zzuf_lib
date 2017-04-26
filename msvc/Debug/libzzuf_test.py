from ctypes import *
import time
import random
MIN_PERCENTAGE = 0.004
MAX_PERCENTAGE = 0.01

class Mutator():
	def __init__(self):
		address = self.load_and_resolve_function('zzuf.dll','zzuf_fuzz_buffer')
		if address == 0:
			print "Error loading zzuf.dll!"
			return
		proto = CFUNCTYPE(c_int, c_int, c_double, c_char_p, c_int) 
		self.mutate_zzuf = proto(address)

	def load_and_resolve_function(self, dll, func):
		handle = windll.kernel32.GetModuleHandleA(dll)
		if handle == 0:
			handle = windll.kernel32.LoadLibraryA(dll)
		if handle == 0:
			return 0
		address = windll.kernel32.GetProcAddress(handle, func)
		windll.kernel32.CloseHandle(handle)
		return address

	def zzuf_mutate(self, buffer, seed, ratio):
		# We need to copy the buffer since it is going to be directly modified by zzuf
		# This is a little hack to force the creation of a new string
		temp = "%s" % buffer
		buf = c_char_p(temp)
		self.mutate_zzuf(c_int(seed), c_double(ratio), buf, c_int(len(buffer)))
		return buf.value
	
	def generate_new_input(self, template):
		percentage = random.randrange(MIN_PERCENTAGE, MAX_PERCENTAGE)
		return self.zzuf(template, random.randint(0xFFFFFFFF), percentage)

# We use this code to test the fuzzer	
if __name__ == "__main__":
	i = 1
	input = "A" * 1024
	start = time.time()
	m = Mutator()
	#for 10 secs
	while time.time() - start < 10 :
		m.zzuf_mutate(input, i, 0.001)
		i +=1
	print "%d mutations in 10 secs" % i
	
	
	
