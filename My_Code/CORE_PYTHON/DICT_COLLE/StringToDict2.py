#S.split([chars]) -> list
s="ramesh=38,suresh=34,nani=34,roja=18"
print("str : ",s)

lst=s.split(",")  #['ramesh=38','suresh=34']
print(lst)

import time
stu={}
for i in lst:
    time.sleep(.2)
    lst2=i.split("=")
    k,d=lst2
    stu.update({k:int(d)})
    
print("stu : ",stu)
    
