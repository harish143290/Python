
import time

n=int( input("Enter a number : ") )

i=1
while i<=10:
    time.sleep(.5)
    print(n,"x",i,"=",n*i)
    i=i+1
