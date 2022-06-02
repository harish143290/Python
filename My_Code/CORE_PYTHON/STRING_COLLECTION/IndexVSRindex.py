#       0 12 34 5 6
#S="WELCOME"
#S.index(sub[,start,end] ) -> int | ValueError
#S.rindex(sub[,start,end]) -> int | ValueError

s="WELCOME"
print("Data is : ",s)
pos=s.index("E")
print("Found @ : ",pos)

pos=s.index("E",3,7)
print("Found @ : ",pos)

pos=s.rindex("E")
print("Found @ : ",pos)

pos=s.rindex("E",3,7)
print("Found @ : ",pos)



