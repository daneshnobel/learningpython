import os
from os import path

print("The OS is "+os.name)

myFilePath = "sample.txt"
if path.exists(myFilePath):
    print("file sample.txt exists")
    fullPath = path.realpath(myFilePath)
    print("The full path of the file is " +fullPath)
    pt = path.split(fullPath)
    print("split the folder path is "+ pt[0]+" and the file is  "+pt[1])

