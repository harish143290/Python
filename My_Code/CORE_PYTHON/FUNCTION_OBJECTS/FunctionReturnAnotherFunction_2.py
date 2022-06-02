def OuterFun():
    def InnerFun():
        x=10
        return x

    a=InnerFun()
    return a
    
#calling
r=OuterFun( )
print("Result is : ",r)

'''1. if u want use the result of inner function inside of
outer function then inner function need to return
the result

2.if u want use the result of inner function outside of
the outer function then outer function need to return
result of  the inner function. '''


