
''' Function with args and without return
value '''

def myAdd(x,y): # x,y are formal arguments
    s=x+y
    print("Sum is : ",s)

#calling
myAdd(10,20) # 10 and 20 are actual arguments
myAdd(5+5+5,20*3)
a,b=90,90
myAdd(a,b)

''' Formal arguments vs actual arguments
    * Formal arguments are nothing but the arguments
    which are declared in the function def.

    * Formal arguments must be variable
    * Formal arguments acts as local variable
    * Formal arguments are copies of actual arguments.

    # actual arguments are nothing but arguments
    which we are passing by the time calling of function.

    # actual arguments can be variables | expressions |
       values
'''
    
