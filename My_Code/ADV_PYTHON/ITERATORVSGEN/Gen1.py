
import time

def myfun():
    return "shashi"

s=myfun()
print("Type is : ",type(s))
print("Result is : ",s)
print("----------------------------")

def myfun2():
    yield "shashi"
    yield "sudha"
    yield "ramesh"
    yield "roja"

s2=myfun2()
print("Type is : ",type(s2))
print("Generator object :",s2)

import time
for i in s2:
    time.sleep(.2)
    print(i)


