
def OuterFunction():
    y=20 #local variable 
    def InnerFunction():
        x=10 #local variable
        print("Inside of InnerFun ")
        print("x val is : ",x)
        print("y val is : ",y)

    InnerFunction()
    print("Inside of OuterFun")
    print("y val is : ",y)
    # print("x val is : ",x) NameError

#calling
OuterFunction()


    
