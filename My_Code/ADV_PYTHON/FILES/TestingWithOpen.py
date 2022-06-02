
import time

f=open("mydata.txt","w")
time.sleep(1)
print("Is File Closed ? : ",f.closed)
time.sleep(1)
f.close()
print("Is File Closed ? : ",f.closed)
print("--------------------------------------")


with open("mydata2.txt","w") as f2:
    time.sleep(1)
    print("Inside of with block ")
    print("Is File Closed ? : ",f2.closed)

time.sleep(1)
print("Outside of with block")
print("Is File Closed ? : ",f2.closed)




    
    
