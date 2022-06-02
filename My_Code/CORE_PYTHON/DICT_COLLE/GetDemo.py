#D.get(k[,d]) -> value | default value of d is None

stu={"sno":101,"sname":"sai"}
print("stu : ",stu)

name=stu['sname']
print("Name is : ",name)

n1=stu.get('sname')
print("Name is : ",n1)

c=stu.get('scity')
print("city is : ",c)

c=stu.get('scity','xxx')
print("city is : ",c)
