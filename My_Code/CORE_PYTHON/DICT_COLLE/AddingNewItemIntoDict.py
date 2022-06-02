d1={}

#D.update({k:d})
#for adding new item
d1.update({"sno":101})
print("After  Adding : ",d1)

#for updating existed key with new value
d1.update({"sno":222})
print("After updating existed key : ",d1)

#for updating an existed dict with another dict
d2={"sname":"ramesh","scity":"hyd"}
d1.update(d2)  #d1=d1+d2
print("After updating dict with another : ")
print(d1)
