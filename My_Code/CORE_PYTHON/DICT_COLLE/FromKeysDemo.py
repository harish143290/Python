
#D.fromkeys(iterable,value=None) -> dict

lst=["sai","cnu","anu","nani"]
stu={}
stu=stu.fromkeys(lst) #{"sai":None,"cnu":None,......}
print("stu : ",stu)
print("========================================")

stu=stu.fromkeys(lst,"Python")
print("stu : ",stu)

