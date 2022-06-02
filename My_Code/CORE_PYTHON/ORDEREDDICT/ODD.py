
import collections

od=collections.OrderedDict()
print("Type is : ",type(od))
print("OrderedDict : ",od)

od.update({"sno":101})
od.update({"sname":"roja"})
od.update({"sage":23})

import time

for k,d in od.items():
    time.sleep(1)
    print(k,d,sep='--->')

print("Keys ",od.keys())
print("Values : ",od.values())
print("Items : ",od.items())



    




