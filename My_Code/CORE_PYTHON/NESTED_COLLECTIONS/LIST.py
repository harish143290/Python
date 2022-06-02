''' Nested Collection
        - it is the process of defining the any collection
           inside another collection '''

#    0       1          2      3                  4  #       5                                     6
lst=[10,2.2,(10+20j),[11,22,33],(1.1,2.2,3.3),{"aaa","bbb","ccc"},{"sno":101,"sname":"sai"} ]

print("List : ",lst[3])
print("Tuple : ",lst[4])
print("Set : ",lst[5])
print("Dict : ",lst[6])

print("Second Element From List : ",lst[3][1]) #22
print("Sname From dict : ",lst[6]['sname']) #sai
print("Sname From dict : ",lst[6].get('sname'))

import time
for k,d in lst[6].items():
    time.sleep(1)
    print(k,d,sep=" ---> ")
    




