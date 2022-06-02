
import sys
import datetime

def myfun1():
    lst=[i for i in range(1,100001)]
    return lst

def myfun2():
    t=(i for i in range(1,100001))
    return t

'''
f1=myfun1()
print("type is : ",type(f1))
f2=myfun2()
print("type is : ",type(f2))
'''

lst=myfun1()
print("Memory Taken by iterator : ",sys.getsizeof(lst))
st=datetime.datetime.now()
for i in range(1,101):
    myfun1()    
et=datetime.datetime.now()
print("Time Take for iterator : ",et-st)
print("- "*30)

t=myfun2()
print("Memory Taken by gen : ",sys.getsizeof(t))
stg=datetime.datetime.now()
for i in range(1,101):
    myfun2()
etg=datetime.datetime.now()
print("Time Taken for gen : ",etg-stg)






