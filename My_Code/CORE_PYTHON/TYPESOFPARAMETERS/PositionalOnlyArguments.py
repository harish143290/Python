
def myFun(x,y,/):
    print("x val is : ",x)
    print("y val is : ",y)
    print("==============")

#calling
myFun(10,20)
'''
Note:
myFun(x=10,y=20)
TypeError: myFun() got some positional-only arguments
passed as keyword arguments: 'x, y'
'''
