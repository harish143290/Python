
s1={1,2,3}
s2={3,4,5}
print("s1 : ",s1)
print("s2 : ",s2)

s3=s1-s2
print("s1 difference s2 : ",s3)

#S.difference(iterable) -> set
s4=s1.difference(s2)  
print("Result is : ",s4)

#S.difference_update(iterable)
s1.difference_update(s2) #s1=s1-s2
print("Result is : ",s1)
