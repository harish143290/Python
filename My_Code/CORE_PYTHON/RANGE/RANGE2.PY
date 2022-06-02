
import time

#range(stop) -> range object is also an iterable
#range(start,stop[,step]) -> range objet | default stp value is +1

r=range(1,11,1)
print("Type is : ",type(r))
print("Range object : ",r) # range(1,10)

for i in r:
    time.sleep(.2)
    print(i)
    
print("=========================")

r=range(2,21,2)
for i in r:
    time.sleep(.2)
    print(i)

print("==========================")

for i in range(10,0,-1):
    time.sleep(.2)
    print(i)











