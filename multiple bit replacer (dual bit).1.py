#!/usr/bin/python

import binascii
import sys
import os


ext = ".exe"
start = 0
end = 10#os.path.getsize(filename+ext)

for files in os.listdir("."):
	if files.endswith(ext):
		read = open(files,'rb')
		read = read.read()
		rem = end-start
		os.mkdir("temp")
		for i in range(start,end):
			rem-=1
			os.system('cls')
			print ("process folder number: " + str(i) + "\nfolder remaining: " + str(rem))
			address = int(i)
				
			start = read[:address]
			end = read[address+2:]
				
			dir = "temp\\temp"+str(i)
				
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

			for ii in range(0,0xff+1):
				a = hex(ii)
				cut = a[2:]
				if cut == "0" or cut == "1" or cut == "2" or cut == "3" or cut == "4" or cut == "5" or cut == "6" or cut == "7" or cut == "8" or cut == "9" or cut == "a" or cut == "b" or cut == "c" or cut == "d" or cut == "e" or cut == "f":
					cut = "0" + cut 
				byte1 = toAscii(cut)
				for iii in range(0,0xff+1):
					b = hex(iii)
					cutt = b[2:]
					if cutt == "0" or cutt == "1" or cutt == "2" or cutt == "3" or cutt == "4" or cutt == "5" or cutt == "6" or cutt == "7" or cutt == "8" or cutt == "9" or cutt == "a" or cutt == "b" or cutt == "c" or cutt == "d" or cutt == "e" or cutt == "f":
						cutt = "0" + cutt 
					byte2 = toAscii(cutt)
				
					payload = start + byte1+ byte2 + end
					
					write = open(dir + "\\" + cut + "-" + cutt + ext,'wb')
					write.write(payload)
					write.close()
