
import time

n=int(input("Enter a number : "))
cnt=0

for i in range(1,n+1):
    if n%i==0:
        print(i)
        cnt+=1

print("No.of.Fact : ",cnt)
print("Prime ") if cnt==2 else print("Not Prime")
    
