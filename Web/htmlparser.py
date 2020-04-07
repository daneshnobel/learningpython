from html.parser import HTMLParser
import os
 
 #vars global
metacount = 0
    
class MyHTMLParser(HTMLParser):
    
   

    def handle_starttag(self, tag, attrs):
        global metacount
        print("Encountered Tag : ",tag)
        if tag == "meta":
            metacount = metacount+1
        pos = self.getpos()
        
        print("\tAt Line: "+ str(pos[0])+" position: "+str(pos[1]))

        if attrs.__len__() > 0 :
         print("\tAttributes:")
         for attr in attrs:
            print("\t",attr[0]," = ",attr[1])

    def handle_comment(self, data):
        print("Encountered comment: ",data)
        pos = self.getpos()
        print("\tAt line: ", pos[0]," position "+pos[1])
        
    def handle_data(self, data):
        print("Encountered data: ",data)
        pos = self.getpos()
        print("\tAt line: ",pos[0]," position: ",pos[1])

    def handle_endtag(self, tag):
        print("End position of the tag")
        print("\t"+str(self.getpos()))

    # def handle_data(self, data):
       


def main():
    parser = MyHTMLParser()
    print(os.path.expanduser('~/dev/LinkedInLearning/PythonLearn/Web/sample.html'))
    with open(os.path.expanduser('~/dev/LinkedInLearning/PythonLearn/Web/sample.html'), 'r') as f:
        if f.mode == 'r':
            contents = f.read()
            parser.feed(contents)
            print("Number of meta tags found :"+ str(metacount))

if __name__ == "__main__":
    main()