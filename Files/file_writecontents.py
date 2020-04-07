#open a file for writing and create it if it doesn't exist
f = open("sample.txt","w+")

for i in range(1,11):
    f.write("This is the line "+str(i)+"\r\n")

f.close()