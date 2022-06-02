



stu={"sno":101,"sname":"ramesh","scity":"hyd"}
print("Student : ",stu)

k=input("Enter key : ") #scity
if k in stu.keys():
    d=stu[k]
    print("Value of Given Key : ",d)
else:
    print("Sorry Invalid Key ")
