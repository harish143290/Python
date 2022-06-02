
'''Note :
   Here x,y are acts act positional only
   arguments , where as a and b arguments
   can be positional argument or keyword arguments '''

def myFun(x,y,/,a,b):
    print("x val is : ",x)
    print("y val is : ",y)
    print("a val is : ",a)
    print("b val is : ",b)
    print("============")
    
#calling
myFun(10,20,30,40)
myFun(10,20,a=30,b=60)

