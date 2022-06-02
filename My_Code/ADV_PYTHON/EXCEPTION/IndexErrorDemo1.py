#      0     1     2             3               4
lst=[10,2.2,(10+20j),"shashi","python"]
print("List : ",lst)

pos=int(input("Enter Index pos : "))  #3

if pos<len(lst):
    item=lst[pos]
    print("Item @ given Index : ",item)
else:
    print("Sorry Invalid Index ")
