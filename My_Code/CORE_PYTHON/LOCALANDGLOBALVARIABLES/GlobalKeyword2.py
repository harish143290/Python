
x=30 #global variable

def myfun1():   
    global x
    x=x+10
    print("myfun1 ")
    print("x val is : ",x)

#calling
myfun1( )
print("Outside of all the function")
print("global x is : ",x)
