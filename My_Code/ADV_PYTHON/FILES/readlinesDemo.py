import time

f=open("data4.txt")
lst=f.readlines()
print(lst)

for i in lst:
    time.sleep(1)
    print(i,end='')
