
import time

with open("TestingWithOpen.py","r") as f:    
    data=f.read()
    for i in data:
        time.sleep(.1)
        print(i,end='')

