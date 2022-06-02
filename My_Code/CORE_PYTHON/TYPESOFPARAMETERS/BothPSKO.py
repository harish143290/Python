
def myFun(x,y,/,*,a,b):
    print("x val is : ",x)
    print("y val is : ",y)
    print("a val is : ",a)
    print("b val is : ",b)
    print("==================")

#calling
myFun(10,20,a=10,b=20)
'''
myFun(x=10,y=20,a=30,b=40)
TypeError: myFun() got some positional-only arguments
passed as keyword arguments: 'x, y'
'''

'''
myFun(10,20,30,40)
TypeError: myFun() takes 2 positional arguments
but 4 were given
'''


    
