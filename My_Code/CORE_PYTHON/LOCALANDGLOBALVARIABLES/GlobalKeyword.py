
def myfun1():
    global x
    x=10
    print("myfun1 ")
    print("x val is : ",x)

def myfun2( ):
    print("myfun2 ")
    print("x val is : ",x)

#calling
myfun1( )
myfun2( )
print("From outside of all the functions")
print("x val is : ",x)
