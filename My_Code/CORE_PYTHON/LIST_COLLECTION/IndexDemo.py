
#L.index(item[,start,end]) -> int | ValueError

#      0    1    2    3   4    5 [index]
lst=[10,20,30,40,50,30]
print("List : ",lst)
pos=lst.index(30)
print("Found @ : ",pos)

pos=lst.index(130,3,6)
print("Found @ : ",pos)


