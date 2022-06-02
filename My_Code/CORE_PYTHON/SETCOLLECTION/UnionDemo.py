
s1={1,2,3}
s2={3,4,5}
print("s1 : ",s1)
print("s2 : ",s2)

s3=s1 | s2
print("s1 union s2 : ",s3)

#S.union(iterable) -> set
s4=s1.union(s2)
print("s1 union s2 : ",s4)

#S.update(iterable)   set concatenation
s1.update(s2) # s1=s1|s2
print("Result is : ",s1)

