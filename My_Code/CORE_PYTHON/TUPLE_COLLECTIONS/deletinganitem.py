#    0   1    2   3    4   5
t=(10,20,30,40,50,60)

print("Tuple : ",t)

pos=int(input("Enter Index Pos : ")) #2

if pos<len(t):
    f=t[0:pos:1]
    s=t[pos+1: ]
    t=f+s
    print("After Deleting an item : ",t)
else:
    print("Sorry Invalid Index ")
