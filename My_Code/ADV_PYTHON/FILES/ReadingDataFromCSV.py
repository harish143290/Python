
import csv
import time

f=open("stu3.csv","r")
cro=csv.reader(f)

for lst in cro:
    time.sleep(1)
    print(lst[0],"\t",lst[1])
