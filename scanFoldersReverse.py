#!usr/bin/env python

# testing codes here

import os

path0 = os.getcwd()
path = "C:\\Program Files\\Common Files\\bitdefender command line 7.0.0.2639"
files = os.listdir("temp")
desSort_files = sorted(files,reverse=True)
os.chdir(path)

for items in desSort_files:
	print items
	item = os.path.join(path0, items)
	#os.system("pause")
	scan_path = "bdc.exe \""+ path0 + "\\temp" + "\\" + items + "\"" + " -del "
	os.system(scan_path)
		
raw_input("press enter to exit")
