f = open("sample.txt","r")

if f.mode == "r":
    contents = f.read()
    print(contents)