#!/usr/bin/python

import binascii
import sys
import os,shutil, time
import win32com.client

ext = ".doc" #file extension
#block = 50	#block size.
cwd = os.getcwd()

def killFile(ap):
	os.system("C:\\windows\\system32\\taskkill /im " + ap + " /f")

def scan(fldr):
	avpath = "C:\\Program Files\\McAfee\\VirusScan"
	pathscan = os.getcwd()
	os.chdir(avpath)
	os.system("mcodsscan.exe -pupaction remove -fd \""+fldr+"\"")
	os.chdir(pathscan)
	
def runFiles(fldr):
	path = os.getcwd()
	for folders in os.listdir(fldr):								#temp dir
		folderpath = path+ "\\"+fldr+"\\" + folders
		fl = []
		i = 0
		for files in os.listdir(folderpath):
			try:
				Application = win32com.client.Dispatch("Word.Application") 
				Application.Visible = False
			except:
				killFile("winword.exe")
				time.sleep(2)
				Application = win32com.client.Dispatch("Word.Application") 
				Application.Visible = False
				
			fileName, fileExtension = os.path.splitext(files)
			fopen = open(path+"\\log.txt", 'ab')
			fopen.write(fileName+"\r\n")
			fopen.close()
			if files.endswith(".doc") or files.endswith(".docx"):
				print files
				try:
					word = Application.Documents.Open(folderpath+"\\"+files)
					# raw_input("please exit now")
						
				except Exception as e:
					print e
					# raw_input("please exit now")
			try:
				Application.Quit()
			except Exception as e1:
				print e1
				# flag = os.system("tasklist | findstr \"calc.exe\"")
				# if flag == 0:
					# print "Calc executed in file : "+files
					# # print "flag :", flag
					# os.system("pause")
			fl.append(files)		
			if i>0:
				os.remove(folderpath+"\\"+fl[i-1])
			i += 1
			killFile("winword.exe")

def delete(fldr):
	path = os.getcwd()
	for folder in fldr:
		try:
			os.remove(path+"\\"+fldr+"\\"+folder)
		except:
			pass
			
for files in os.listdir("."):
	if files.endswith(ext):
		read = open(files,'rb')
		read = read.read()

		# from array import *
		a=[155, 156, 157, 158, 159, 160, 161, 162, 163, 200, 332, 333, 334, 335, 2596, 2597, 2598, 2599, 2600, 2601, 2602, 2603, 2604, 2605, 2606, 2607, 2608, 2609, 2610, 2611, 2612, 2613, 2614, 2615, 2616, 2617, 2618, 2619, 2620, 2621, 2622, 2623, 2624, 2625, 2626, 2627]

		try:
			os.mkdir("temp")
		except:
			shutil.rmtree("temp")
			os.mkdir("temp")
			
		count = 1
		for i in a:
			if (count%2) == 0:
				scan(cwd+"\\temp")
				runFiles("temp")
				delete("temp")
				# os.system("pause")
				
			count += 1
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
