
import csv,time

f=open("stu3.csv","r")
cro=csv.reader(f)

for lst in cro:
    time.sleep(1)
    for i in lst:
        print(i,end='\t')
    print(" ")
