"""                                                      #
    ####    ####   ####   ##   ####  ####        #      ##
    ####    ####   #### ##     ####  ####       ###   ##### 
  #################### # ######### ## #####    ##### ######
   ####    ####   ####  ##    #### ## ####     ##### #####
   ####    ####   ####    ##  ####    ####      ###  ###
                                                 #   ##
# ENJOY!!                                            #
"""
import os, shutil

for folder in os.listdir("."):
	print folder
	fileName, fileExtension = os.path.splitext(folder)
	print fileName + "      " + fileExtension
	if fileExtension =="":
		files = os.listdir(folder)
		#sizeOfFolder = os.path.getsize(files)
		if (len(files) == 0):
			shutil.rmtree(folder)
