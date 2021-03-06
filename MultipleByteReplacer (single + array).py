#!/usr/bin/python

import binascii
import sys
import os,shutil


ext = ".exe"

for files in os.listdir("."):
	if files.endswith(ext):

		read = open(files,'rb')
		read = read.read()

		from array import *
		a=array('i',[10,20,100,200,300])	#starting position of block.
		try:
			os.mkdir("temp")
		except:
			shutil.rmtree("temp")
			os.mkdir("temp")
			
		block = 300	#block size.
		for i in a:
			
			def toAscii(n):
					"""
					Converts a byte to its ascii equivalent. Null byte = space

					Arguments:
					n - A string (2 chars) representing the byte to convert to ascii

					Return:
					A string (one character), representing the ascii equivalent
					"""
				
					asciiequival=binascii.a2b_hex(n)
					return asciiequival
					
			for j in range(i,i+block):
				print ("process byte number: " + str(j))
				start = read[:j]
				end = read[j+1:]
					
				byte = toAscii("00")
			
				payload = start + byte + end
			
				write = open("temp\\" + str(j) + " - 00" + ext,'wb')
				write.write(payload)
				write.close()
