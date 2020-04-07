class myClass():
    def method1(self,strMessage):
        print("myClass1 -- method1 -- "+strMessage)
    def method2(self,strMessage):
        print("myClass1 -- method2 -- "+strMessage)

class myAnotherClass(myClass):
    def method1(self,strMessage):
        print("myAnotherClass -- method1 -- "+strMessage)
    def method2(self,strMessage):
        myClass.method2(self,"Again from World 1")
        print("myAnotherClass -- method2 -- "+strMessage)

inst1 = myClass()
inst1.method1("Hello")
inst1.method2("World")

inst2 = myAnotherClass()
inst2.method1("anoth Hello")
inst2.method2("anoth World")