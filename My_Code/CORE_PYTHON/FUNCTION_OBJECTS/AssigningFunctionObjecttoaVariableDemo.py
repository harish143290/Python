''' function object demo '''
def myfun():
    print("Hello")

print("Type is : ",type(myfun))
print("Hcode is : ",myfun)
myfun( )

print("- "*30)

x=myfun
print("Type is : ",type(x))
print("Hcode is : ",x)
x( )

print("- "*30)
print(myfun())

