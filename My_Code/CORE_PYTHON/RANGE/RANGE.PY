
import time

#range(stop) -> range object

r=range(10)
print("Type is : ",type(r)) #<class 'range'>
print("Range object : ",r) #range(0,10) stop value is not included

for i in r:
    time.sleep(.2)
    print(i)
