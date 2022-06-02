
import time

f=open("data4.txt","r")
data=f.read()
print(data)

for i in data:
    time.sleep(.1)
    print(i,end='')
    
f.close()


       
