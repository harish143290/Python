def OuterFun():
    def InnerFun():
        x=10
        return x

    return InnerFun   
    
#calling
ifr=OuterFun( ) #ifr is the copy of InnerFun
a=ifr( ) #ifr( ) calling InnerFun( )
print("Result of Inner Fun : ",a)

'''1. if u want use the result of inner function inside of
outer function then inner function need to return
the result

2.if u want use the result of inner function outside of
the outer function then outer function need to return
result of  the inner function.

3.if u want use the inner function outside of the outer
function then outerfunction need to return inner fun'''






