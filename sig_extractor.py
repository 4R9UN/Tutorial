import os, binascii
import pefile
files = os.listdir("temp")
for i in range(0,len(files)):
    files[i] = files[i][:files[i].find("-")-1]
    #print files[i]
rd = open("temp.exe",'rb').read()
#pe = pefile.PE('C:\Users\john cusack\Desktop\ollydbg.exe')
#for section in pe.sections:
    #print section.Name
    #print hex(section.VirtualAddress)
    #print hex(section.Misc_VirtualSize)
    #print format(section.SizeOfRawData,"x")
files.sort(key=int)
print files
temp = ""
for i in range(0,len(files)):
    temp+=str(files[i]) + "\t\t" + format(int(files[i]),"x") + "\t\t" + binascii.hexlify(rd[int(files[i])])+ "\n"
fl = open("report.txt",'wb')
fl.write(temp)
fl.close()
os.system("report.txt")

    

 

