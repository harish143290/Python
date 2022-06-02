
lst=[[10,20,30],(1.1,2.2,3.3),{"aaa","bbb","ccc"},
         {"sno":101,"sname":"ramesh","scity":"Hyd"} ]

import time

for i in lst:
    if isinstance(i,dict):
        print("Type is : ",type(i))
        print("Data is : ",i)

        for k,d in i.items():
            time.sleep(1)
            print(k,d,sep=' ----> ')
        
    else:    
        time.sleep(1)
        print("Type is : ",type(i))
        print("Data is : ",i)

        for j in i:
            time.sleep(.5)
            print(j)
        
    print("==========")
