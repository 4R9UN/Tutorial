#insert tool

import binascii
import sys
import os

filename = "abc"
ext = ".rar"
bit = "\x23"
start =0
end = os.path.getsize(filename+ext)
read = open(filename+ext,'rb')
read = read.read()

dir = "temp"
	
try:
		os.mkdir(dir)
except:
		try:
			os.rename(dir,dir + ".old")
		except:
			print ("#Directory Already Exist\n"
				   "#Delete Old temp Directory")	
		try:
			os.mkdir(dir)
		except:
			print " "



for i in range(start,end):
	print ("process bit number: " + str(i))
	s = read[0:i]
	e = read[i::]
	payload = s + bit + e
	write = open(dir + "\\" + filename + "_" + str(i) + ext,'wb')
	write.write(payload)
	write.close()
