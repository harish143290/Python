
import random
import time

lst=['pen','book','box','pencil','mouse','printer']
print("List : ",lst)

for i in range(1,11):
    time.sleep(1)
    print( random.choice(lst) )
    
