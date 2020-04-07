f = 0


def foo():
    f= "now it is a string"
    print(f)




def boo():
    global f
    f = "now changing the value of f outside from inside a func"
    print(f)

print(f)
foo()
print(f)
print("Value again retained to 0 because now the scope got changed to global and the value of global f is being printed out")
boo()

