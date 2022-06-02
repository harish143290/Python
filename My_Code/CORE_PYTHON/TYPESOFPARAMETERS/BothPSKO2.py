
'''
def myFun(*,a,b,/,x,y):
    pass

Invalid Syntex
'''

def myfun(a,b,/,c,d,*,e,f):
    print("a val is : ",a)
    print("b val is : ",b)
    print("c val is : ",c)
    print("d val is : ",d)
    print("e val is : ",e)
    print("f val is : ",f)
    print("================")

#calling
myfun(10,20,33,44,e=5.5,f=6.6)
myfun(10,20,c=33,d=44,e=5.5,f=6.6)
'''Note:
  in this function
  a,b are positional only arguments
  c,d work as positional arguments | keyword arguments
  e,f work as keyword only arumgnets '''








    
    

