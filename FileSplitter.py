import os, shutil

block = 300

for files in os.listdir("."):
	fileName, fileExtension = os.path.splitext(files)
	if fileExtension !=".py" and len(fileExtension) != 0:
		ext = fileExtension
		end = os.path.getsize(files)
		read = open(files,'rb').read()
		strt = 0
		rem = end/block
		dir = fileName
		try:
				os.mkdir(dir)
		except:
				shutil.rmtree(dir)
				os.mkdir(dir)
		
		for i in range(0,end/block):
			print "block remaining - " + str(rem)
			rem-=1
			for j in range(0,block):
				temp = read[:strt] + "\x00" * block + read[strt+block:]
			fname = dir + "\\" + str(strt) + " - " + str(strt+block) + ext
			write =  open(fname,'wb')
			write.write(temp)
			strt += block 
			
					
