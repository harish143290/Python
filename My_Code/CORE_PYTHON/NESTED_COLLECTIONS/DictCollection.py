import time

stu={"Sno":101,"Sname":"Ramesh","Address":{"Hno":"1-2-3","Street":"Prasanthi Hills","Roadno":"1A/a","City":"Hyderabad"}, "Marks":[40,50,60,70,80,30]}
print(type(stu))
print(stu.keys())

for k,d in stu.items():
    if isinstance(d,dict):
        print(k)
        for a,b in d.items():
            time.sleep(1)
            print("    ",a,"--->",b)
            
    elif isinstance(d,list):
        print(k)
        s=0
        for i in d:
            time.sleep(.2)
            print("    ",i)
            s=s+i
        print("-----------")
        print("Total ",s)

    else:
        print(k,"   -----> ",d)


'''
Output:
Sno -> 101
Sname -> Ramesh
Address:
    Hno : xxx
    Street : xxx
    Road No : xxx
    City : xxx
Marks:
    40
    50
    60
    70
    80
    30
=====
   xxxx   '''
