#D.copy( ) -> dict
d1={"sno":101,"sname":"ramesh","scity":"hyd"}
print("D1 : ",d1)

d2=d1.copy()
print("D2 : ",d2)

d1.update({"spin":500090})
print("After modification d1 : ")
print("D1 : ",d1)
print("D2 : ",d2)

