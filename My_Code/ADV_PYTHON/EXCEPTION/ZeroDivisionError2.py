
x=int(input("Enter a number : "))
y=int(input("Enter b number : "))
try:
    z=x/y
except ZeroDivisionError:
    print("Sorry V R N D By Zero...!!!")
else:
    print("Result is : ",z)
