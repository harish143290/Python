import csv

f=open("stu3.csv","w",newline='')
cwo=csv.writer(f)
cwo.writerow(["sno","sname","scity"])

while True:
    no=int(input("Enter sno : "))
    name=input("Enter name : ")
    city=input("Enter city : ")
    cwo.writerow([no,name,city])

    opt=input("Do u want another Rec Y|N ")
    if opt in ['N','n']:
        break
    
print("Rec is Saved")
f.close()
