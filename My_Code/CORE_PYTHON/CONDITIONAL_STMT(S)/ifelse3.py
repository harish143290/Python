'''Accept year from the user findout the given year is
leap or not '''

''' Accept 2 numbers from the user findout the biggest in
two '''

a=int(input("Enter a number : "))
b=int(input("Enter b number : "))

if a>b:
    print("biggest is : ",a)
else:
    print("biggest is : ",b)

print("biggest  is : ",a) if a>b else print("biggest is :",b)
