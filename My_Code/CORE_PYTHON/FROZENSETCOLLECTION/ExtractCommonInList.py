#S.intersection(iterable) -> set
#FS.intersection(iterable) -> FS | iterable
#frozenset(iterable) -> frozenset

lst1=[10,20,30]
lst2=[30,20,50]

f1=frozenset(lst1)
f2=frozenset(lst2)

print("f1 : ",f1)
print("f2 : ",f2)

f3=f1.intersection(f2)
print("Result is : ",f3)

#list(iterable) -> list
lst3=list(f3)
print("Result is : ",lst3)

#App-2
lst3=list(frozenset(lst1).intersection(frozenset(lst2)))
print("Result is : ",lst3)










