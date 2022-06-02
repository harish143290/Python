stu={"sno":101,"sname":"ramesh","scity":"hyd"}

#D.items( ) -> <class 'dict_items'> | iterable
#dict_items is collection of items in the form of tuple

import time
items=stu.items()
print("Type is : ",type(items))
print("Items are : ",items)

for item in items:
    time.sleep(1)
    #print(item) #here item is a tuple
    k=item[0]
    v=item[1]
    print(k,v,sep='---->')    
print("- "*30)

#App-2
for item in items:
    time.sleep(1)
    k,d=item #unpacking
    print(k,d,sep='<--->')
print("- "*30)

#App-3
for k,d in items:
    time.sleep(1)
    print(k,d,sep='<<>>')
print("-"*30)
    




    
    











