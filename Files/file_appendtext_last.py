#open a file and create it if it doesnt exist
#but if exists, append the text to be written at the end of the file

f = open("sample.txt","a")

for i in range(1,11):
    f.write("This is the line "+str(i)+"\r\n")

f.close()