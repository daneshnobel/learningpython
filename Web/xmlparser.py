import xml.dom.minidom
import os

def main():
    print(os.path.expanduser('~/dev/LinkedInLearning/PythonLearn/Web/samplexml.xml'))
    doc = xml.dom.minidom.parse(os.path.expanduser('~/dev/LinkedInLearning/PythonLearn/Web/samplexml.xml'))
    print("Document name",doc.nodeName)
    print("\tFirst Node", doc.firstChild.nodeName)
    #print("\tand the first tag is ",doc.firstChild.tagName)
    skills = doc.getElementsByTagName("skill")
    print("\tTotal Skills: %d" % skills.length)
    for skill in skills:
        #print("\t\t",skill.getAttribute("name"))
         skillName = skill.firstChild.data
         print("\t\t%s" %skillName)
        # attrs = skill.attributes.items()
        # print(attrs)

        
if __name__ == "__main__":
    main()
