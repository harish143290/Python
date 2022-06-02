#S.split([chars]) -> list
#converting list to dict collection using fromkeys

s="ramesh suresh rajesh mahesh"
print("str : ",s)

lst=s.split() #['ramesh','suresh',........]

stu={}
stu=stu.fromkeys(lst)
print("stu : ",stu)
