import os
import subprocess

path = os.getcwd()
for file in os.listdir("temp"):
	print file
	filepath = path +"\\temp\\"+ "\"" + file + "\""
	command = "start " + filepath
	#handle = os.system(command)
	#handle = subprocess.Popen("start "+ filepath, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if os.system(command) == 0:
		os.system(command)
	
task = 	"tasklist | findstr \".00.exe\" \> log.txt"
os.system(task)