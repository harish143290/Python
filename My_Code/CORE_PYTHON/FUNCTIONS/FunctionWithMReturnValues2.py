
def myCalc(x,y):
    a=x+y
    s=x-y
    m=x*y
    d=x/y
    return a,s,m,d

#calling
t=myCalc(10,2)
print(type(t))
print("Result is : ",t)

print("Addition is : ",t[0])
print("Sub is : ",t[1])
print("Mul is : ",t[2])
print("Division is : ",t[3])
