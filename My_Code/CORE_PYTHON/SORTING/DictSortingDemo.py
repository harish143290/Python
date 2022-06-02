
'''
  sorted(iterable,key=None,reverse=False) -> list
                iterable is list | tuple | set | str | dict ...

D.keys( ) -> <class 'dict_keys'>
D.values( ) ->   <class 'dict_values'>
D.items( )  -> <class 'dict_items'>
                               7032 7032 53 | 54 
'''

stu={"b":"balu","a":"anu","c":"cnu","d":"dhanu"}
print("stu : ",stu)
lst=sorted( stu.keys( ) )
print("After Sorting Keys : ",lst)
print("- "*40)

lst=sorted( stu.values( ) )
print("After Sorting values : ",lst)
print("- "*40)

lst=sorted( stu.items( ))
print("After Sorting items : ",lst)
print("- "*40)

stu2={}

import time
for i in lst:
    time.sleep(1)
    k,d=i
    stu2.update({k:d})

print("After sorting dict : \n ", stu2)














