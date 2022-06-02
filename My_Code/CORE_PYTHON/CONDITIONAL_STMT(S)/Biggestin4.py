
a=int(input("Enter a number : "))
b=int(input("Enter b number : "))
c=int(input("Enter c number : "))
d=int(input("Enter d number : "))

if a>b and a>c and a>d:
    print("a is big")
elif b>c and b>d:
    print("b is big")
elif c>d:
    print("c is big")
else:
    print("d is big")
