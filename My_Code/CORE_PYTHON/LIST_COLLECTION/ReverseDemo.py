
#L.index(item[,start,end]) -> int | ValueError
#L.count(item[,start,end]) -> int | 0
#L.reverse( )

#      0    1    2    3   4    5 [index]
lst=[10,20,30,40,50,30]
print(lst[len(lst)::-1])
print("List : ",lst)

lst.reverse()
print("Reverse : ",lst)

