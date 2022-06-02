
def OuterFun():
    def InnerFun():
        x=10
        return x

    a=InnerFun()
    print("Result is : ",a)

#calling
OuterFun( )
''' if u want use the result of inner function inside of
outer function then inner function need to return
the result '''
