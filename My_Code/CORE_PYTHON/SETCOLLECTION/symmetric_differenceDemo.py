s1={1,2,3}
s2={3,4,5}
print("s1 : ",s1)
print("s2 : ",s2)

s3=s1^s2
print("s1^s2 ? : ",s3)

#S.symmetric_difference(iterable) -> set
s4=s1.symmetric_difference(s2)
print("s1^s2 ? : ",s4)

#s.symmetric_difference_update(iterable)
s1.symmetric_difference_update(s2) #s1=s1^s2
print("s1^s2 ? : ",s1)

