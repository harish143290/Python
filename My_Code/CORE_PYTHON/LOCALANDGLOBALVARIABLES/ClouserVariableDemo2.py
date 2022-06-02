
def OuterFunction():
    y=20 #clouser variable 
    def InnerFunction():
        nonlocal y
        y=y+20
        print("Inner Function ")
        print("y val is : ",y)

    InnerFunction()
    print("inside of outerfunction")
    print("y val is : ",y)
    
#calling
OuterFunction()


    
