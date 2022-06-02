#       0 12 34 5 6
#S="WELCOME"

#S.count(sub[,start,end] ) -> int

s="WELCOME"
print("Data is : ",s)
#no=s.count("E")

no=s.count("E",3,7)
print("Found For  : ",no," times ")

no=s.count("e")
print("Found For : ",no, "Times ")
