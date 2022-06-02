#       0    1                 2           3               4 
lst=[10,"Ramesh","Hyd","Python",40]

print("List : ",lst)
#len(iterable) -> int
no=len(lst)
print("No.of.Object in the list : ",no)

#Reading values From list  using while
import time

index=0
while index<len(lst):
    time.sleep(1)
    print(lst[index])
    index=index+1

#Reading Values From list using for loop
print("List Element using for...")
for i in lst:
    time.sleep(.1)
    print(i)






