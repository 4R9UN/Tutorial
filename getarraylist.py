import os

path = os.getcwd()
tpath = path+"\\temp"
os.chdir(tpath)
lst = []
for file in os.listdir("."):
	a = file.split("-")
	lst.append(a[0])
print str(lst).replace("'","")

while True:
	pass