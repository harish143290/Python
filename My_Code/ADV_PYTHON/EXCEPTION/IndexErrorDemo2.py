#      0     1     2             3               4
lst=[10,2.2,(10+20j),"shashi","python"]
print("List : ",lst)

pos=int(input("Enter Index pos : "))

try:
    item=lst[pos]

except IndexError:
    print("Sorry Invalid Index")
    
else:
    print("Item @ given index : ",item)
