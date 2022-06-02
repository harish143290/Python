import time

'''App-1
f=open("data4.txt","r")
data=f.read()
for i in data:
    time.sleep(.1)
    print(i,end='')
'''

'''App-2
f=open("data4.txt","r")
for i in f.read():
    time.sleep(.1)
    print(i,end='')
'''

f=open("data4.txt","r")
for i in f:
    time.sleep(.1)
    print(i,end='')
    



