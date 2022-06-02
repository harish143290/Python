
'''accept a number from the user and findout the
given number is odd or even '''

n=int( input("Enter a number ") ) #10

if n%2==0:
    print("Even ")
else:
    print("Odd ")

print("Even ") if n%2==0 else print("Odd")
