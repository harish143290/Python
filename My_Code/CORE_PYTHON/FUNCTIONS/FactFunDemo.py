
def myFact(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f        

#calling
n=int(input("Enter a number : "))
r=myFact(n)
print("Fact is : ",r)

import math
r2=math.factorial(n)
print("Fact is : ",r2)
