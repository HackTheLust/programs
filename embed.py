#!/bin/pthon3
#please provide the output-file-extension as same as cover-file's-extension
#otherwise it will not work
import os
a=input("Specify cover file : ")
b=input("Specify Ember file : ")
print("\nOutput-file-extension must be same as cover-file-extension !!\n")
c=input("Specify output file name : ")
try:
    inp_file1=open(a, "rb").read()
    inp_file2=open(b,"rb").read()
    out_file=open(c,"wb")
    out_file.write(inp_file1)
    out_file.write(inp_file2)
except:
    print("Check for proper file name or path of file")
    quit()
print("Everything is done. File is Embed to "+c)
