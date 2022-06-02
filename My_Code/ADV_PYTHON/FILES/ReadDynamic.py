import time
f=None
try:
    fname=input("Enter Filename : ") 
    f=open(fname,"r")

except FileNotFoundError:
    print("Sorry File Not Found ......")

else:
    data=f.read()
    for i in data:
        time.sleep(.1)
        print(i,end='')

finally:
    if f!=None:
        f.close()
