'''
  sorted(iterable,key=None,reverse=False) -> list
                iterable is list | tuple | set | str | dict ...
'''

lst=[("cnu",34),("anu",23),("balu",27),("dhanu",24)]
print("List : ",lst)

print("Sorting based on the names ")
lst=sorted(lst,key=lambda x:x[0])
import time
for i in lst:
    time.sleep(1)
    print(i)

print("Sorting Based on the ages")
lst=sorted(lst,key=lambda x:x[1],reverse=False)
for i in lst:
    time.sleep(1)
    print(i)




