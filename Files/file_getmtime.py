
import datetime
from datetime import timedelta
import os
from os import path
import time

filePath = "sample.txt"
#t = time.ctime(path.getmtime(path.realpath(filePath)))

td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime(filePath))

print("The file was modified "+str(td)+ " ago... or "+str(td.total_seconds())) 