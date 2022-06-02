#tuple(iterable) -> tuple

#    0   1    2   3    4   5
t=(10,20,30,40,50,60)

print("Tuple : ",t)
pos=int(input("Enter Index Pos : ")) #2

if pos<len(t):
    item=[ int(input("Enter new item : ")) ] #item-> [ 222 ]
    f=t[0:pos]
    s=t[pos:]
    t=f+tuple(item)+s
    print("After Inserting : ",t)
else:
    print("Invalid Pos ")





