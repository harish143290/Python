stu={"sno":101,"sname":"ravi","scity":"kmm"}
print("Student : ",stu)

#D.keys() -> <class 'dict_keys'> | iterable
keys=stu.keys()
print("Type is : ",type(keys))
print("Keys are : ",keys)

import time
for k in keys:
    time.sleep(1)
    print(k)

#D.values( ) -> <class 'dict_values'> | iterable
values=stu.values()
print("Type is : ",type(values))
print("values are : ",values)

for v in values:
    time.sleep(1)
    print(v)




