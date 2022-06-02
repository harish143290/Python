
def myFun(*,x,y):
    print("x val is : ",x)
    print("y val is : ",y)
    print("---------------------")

#calling
myFun(x=10,y=20)
myFun(y=222,x=111)
'''
Note:
myFun(10,20)
TypeError: myFun() takes 0 positional arguments
but 2 were given '''
