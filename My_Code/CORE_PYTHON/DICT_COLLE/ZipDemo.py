#zip(iterable1,iterable2) -> zip object | iterable

lstn=["cnu","anu","nani"]
tc={"Python","Django","MongoDB"}

z=zip(lstn,tc)
print("Type is : ",type(z)) #<class 'zip'>
print("Zip object : ",z)

#dict(iterable) -> dict
stu=dict(z)
print("stu : ",stu)
