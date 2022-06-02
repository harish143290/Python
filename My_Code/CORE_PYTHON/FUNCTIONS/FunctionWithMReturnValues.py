m,
def myCalc(x,y):
    a=x+y
    s=x-y
    m=x*y
    d=x/y
    return a,s,m,d

#calling
a,b,c,d=myCalc(10,2)
print("Addition is : ",a)
print("Sub is : ",b)
print("Mul is : ",c)
print("Division is : ",d)
