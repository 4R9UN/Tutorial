"""                                                      #
    ####    ####   ####   ##   ####  ####        #      ##
    ####    ####   #### ##     ####  ####       ###   ##### 
  #################### # ######### ## #####    ##### ######
   ####    ####   ####  ##    #### ## ####     ##### #####
   ####    ####   ####    ##  ####    ####      ###  ###
                                                 #   ##
# ENJOY!!                                            #
"""

import thread
import os
import time
import sys
import tkMessageBox, Tkinter

app = "POWERPNT.exe"
scriptDirPath = os.getcwd()
desktopPath = "C:\\Documents and Settings\\Administrator\\Desktop"


def openFile(folderName, fileName):
	openFilePath = scriptDirPath + "\\temp\\" + folderName
	print openFilePath
	os.chdir(openFilePath)
	os.system("start " + fileName)

def killFile(ap):
	os.system("C:\\windows\\system32\\taskkill /im " + ap + " /f")
	
for folder in os.listdir("temp"):
	fPath = scriptDirPath + "\\temp"
	# print folder
	# os.system("pause")
	folderPath = os.path.join(fPath, folder)
	for file in os.listdir(folderPath):	
		# print file
		# os.system("pause")
		try:
			thread.start_new_thread(openFile, (folder, file, ))
			#os.system("tasklist | findstr calc > log.txt")
			time.sleep(6)
			killFile(app)
			# thread.start_new_thread(killFile, (app, ))
			# time.sleep(1)
		except:
			print "Error!!"
		#os.chdir(desktopPath)
		
		flag = os.system("tasklist | findstr calc") 
		
		"""if flag = 0 then calc has opened"""
		
		if flag == 0:
			os.system("echo "+file+" >calc.txt")
			window = Tkinter.Tk()
			window.wm_withdraw()
			tkMessageBox.showinfo(title="Update Status", message="Calculator opened successfully!!")
			calc = "calc.exe"
			killFile(calc)
			sys.exit(0)
		os.remove(file)

# while 1:
	# pass
	
