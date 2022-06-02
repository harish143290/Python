
s1={1,2,3}
s2={3,4,5}
print("s1 : ",s1)
print("s2 : ",s2)

s3=s1&s2
print("s1 intersection s2 : ",s3)

#S.intersection(iterable) -> set
s4=s1.intersection(s2)
print("s1 intersection s4 : ",s4)

#S.intersection_update(iterable)
s1.intersection_update(s2) # s1=s1&s2
print("Result is : ",s1)
