#!/usr/bin/python

import binascii
import sys
import os,shutil

ext = ".ppt" #file extension
block = 50	#block size.

for files in os.listdir("."):
	if files.endswith(ext):
		read = open(files,'rb')
		read = read.read()

		# from array import *
		a=[7204, 7205, 7206, 7207, 7230, 7258, 7259, 7260, 7261, 7288, 7290, 7302, 7306, 7318, 8358, 8398, 8610, 8666, 8668, 8670,8672, 8674, 8676, 8678, 8680, 8730, 8732, 8782, 8787, 8802,9434, 9435, 9436, 9437, 9450, 9451, 9452, 9453, 9478, 9479, 9480, 9481, 9518, 9519, 9520, 9521, 9556, 9557, 9558, 9559]	#starting position of block.
		try:
			os.mkdir("temp")
		except:
			shutil.rmtree("temp")
			os.mkdir("temp")
			
		
		for i in a:
			# print i
			# os.system("pause")
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
					
			# for j in range(i,i+block):
			print ("process folder number: " + str(i))
			start = read[:i]
			end = read[i+1:]
			dir = "temp\\temp"+str(i)
			os.mkdir(dir)
			for ii in range(0,0xff+1):
				a = hex(ii)
				cut = a[2:]
			
				if cut == "0" or cut == "1" or cut == "2" or cut == "3" or cut == "4" or cut == "5" or cut == "6" or cut == "7" or cut == "8" or cut == "9" or cut == "a" or cut == "b" or cut == "c" or cut == "d" or cut == "e" or cut == "f":
					cut = "0" + cut 
				byte = toAscii(cut)
			
				payload = start + byte + end
			
				write = open(dir + "\\" + str(i) + "-" + cut + ext,'wb')
				write.write(payload)
				write.close()
