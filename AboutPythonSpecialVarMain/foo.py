def funcA():
    from foo2 import function1
    function1()

funcA()


#Output Command
#Python3 ~/path/foo.py
#Output of this execution
# random statement1
# function1 is on
# random statement2
# function 2 is on
# function1 is on

# You can note from the execution of this file 
#function1() inside funcA has been called --> 
#Since we do not have the __name__ = "main" check inside the function1() of the foo.py module
#all the statements are executed first which is seen in the output from line 11 to line 14
#In Line 15, out function1() has been called
# It is best to have the __main__ check in the file, because if it has been exported as a module to other 
#components, unexpected statements will be executed like the above scenario...

