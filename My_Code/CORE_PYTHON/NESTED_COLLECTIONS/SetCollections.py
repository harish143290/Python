'''
s={[10,20,30],(1.1,2.2,3.3),{"aaa","bbb","ccc"},
      {"sno":101,"sname":"ramesh"}}
                         TypeError: unhashable type: 'list'  
if u want access 20
                        s[0][1]

Add new item inside of set collection which in another
set
       s[2].add("ddd")
       In the set there is no index and slicing


s={(1.1,2.2,3.3),{"aaa","bbb","ccc"},
      {"sno":101,"sname":"ramesh"}}
                         TypeError: unhashable type: 'set'   '''

'''
s={ (1.1,2.2,3.3),{"sno":101,"sname":"ramesh"} }
                                TypeError: unhashable type: 'dict'  '''

import time
s={ (1.1,2.2,3.3),(10,20,30),("aaa","bbb","ccc") }

for i in s:
    time.sleep(1)
    print("Data is : ",i)
    for j in i:
        time.sleep(1)
        print(j)



