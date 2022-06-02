
def OuterFun():
    def InnerFun():
        x=10
        return x

    a=InnerFun()
    print("Result is : ",a)

#calling
OuterFun( )
