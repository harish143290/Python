#tuple(iterable) -> tuple

#    0   1    2   3    4   5
t=(10,20,30,40,50,60)

print("Tuple : ",t)
pos=int(input("Enter Index Pos : ")) #2

if pos<len(t):
    new=[ int(input("Enter new Item : ")) ]
    f=t[0:pos]
    s=t[pos+1:]
    t=f+tuple(new)+s
    print("After update : ",t)
else:
    print("Invalid Index ")
