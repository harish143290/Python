
import csv

f=open("stu1.csv","w")
cwo=csv.writer(f)
cwo.writerow(["sno","sname","sage"])
print("Data is Saved ")
f.close()
