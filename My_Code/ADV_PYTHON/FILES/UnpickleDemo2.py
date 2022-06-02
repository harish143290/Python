
import pickle
import time

f=open("myeinfo2.txt","rb")

while True:
    time.sleep(1)
    try:
        e=pickle.load(f)
    except EOFError:        
        break
    else:
        e.getEmployee()
