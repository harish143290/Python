''' varargs arguments internally works
as a tuple collection '''
import time
def myFun(*x):
    time.sleep(1)
    print("Type is : ",type(x))
    print("Values of x : ",x)
    print("- "*30)

#calling
myFun(10,20,30,40,50)
myFun(10,20,30)
myFun(10)
myFun( )
'''
myFun(x=10)
TypeError: myFun() got an unexpected
keyword argument 'x'  '''


