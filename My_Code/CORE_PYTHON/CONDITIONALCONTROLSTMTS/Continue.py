
import time

for i in range(1,11):
    time.sleep(.5)
    print("Hello ...",i)
    if i==5 or i==7:
        continue
    
    print("MyDear ")
    print("Have a good day ")
    print("-"*20)
