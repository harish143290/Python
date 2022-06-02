
lst=[]
for i in range(1,11):
    lst.append(i)

print("List : ",lst)
print("- "*30)

lst2=[i for i in range(1,11)]
print("Type is : ",type(lst2))
print("Result is : ",lst2)
print("- "*30)

lst3=[i for i in range(2,41,2)]
print("Lst3 : ",lst3)
