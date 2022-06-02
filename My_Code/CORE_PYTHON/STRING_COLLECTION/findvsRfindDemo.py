#       0 12 34 5 6
#S="WELCOME"
#S.find(sub[,start,end] ) -> int | -1
#S.rfind(sub[,start,end]) -> int | -1

s="WELCOME"
print("Data is : ",s)
pos=s.find("E")
print("Found @ : ",pos)

pos=s.find("E",3,7)
print("Found @ : ",pos)

pos=s.rfind("E")
print("Found @ : ",pos)

pos=s.rfind("E",3,7)
print("Found @ : ",pos)

pos=s.find("e")
print("Found @ : ",pos)


