
import threading
import time

def myfun():
    ct=threading.current_thread()
    print(t1.getName()," started its execution....")
    time.sleep(10)
    print(t1.getName()," ends its execution ....")
    

t1=threading.Thread(target=myfun,name="Child-1")
t1.start()
print("Thread is under process : ",t1.is_alive())
time.sleep(12)
print("Thread is under process | isalive ? : ",t1.is_alive())
