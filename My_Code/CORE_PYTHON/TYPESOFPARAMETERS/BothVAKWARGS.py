
import time

def myFun(*x,**y,):
    time.sleep(1)
    print("x val is : ",x)
    print("y val is : ",y)
    print(" - "*20)

#calling
myFun(10,20,30,sno=10,sname="ramesh",scity="hyd")
    
