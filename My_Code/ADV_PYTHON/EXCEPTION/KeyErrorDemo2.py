



stu={"sno":101,"sname":"ramesh","scity":"hyd"}
print("Student : ",stu)

k=input("Enter key : ") #scity
try:
    d=stu[k]
except KeyError:
    print("Sorry Invalid Key ")
else:
    print("Value Of Given Key is : ",d)
