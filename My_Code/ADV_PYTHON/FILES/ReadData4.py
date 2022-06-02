import time

fname=input("Enter Filename : ")
f=None
try:    
    f=open(fname,"r") 
except FileNotFoundError:
    print("Sorry File is not existed ")
else:
    data=f.read()
    for i in data:
        time.sleep(.1)
        print(i,end='')
finally:
    if f!=None:
        f.close()
