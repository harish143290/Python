
#shallowcopy
#L.copy() -> list

lst1=[10,20,30]
lst2=lst1.copy()
print("lst1 : ",lst1)
print("lst2 : ",lst2)

lst1[1]=222
print("After modification ")
print("lst1 : ",lst1)
print("lst2 : ",lst2)
