import time
import threading

def myfun():
    ct=threading.current_thread()
    print(ct.getName()," started its Execution ....")
    time.sleep(5)
    print(ct.getName()," Ends its Execuction .... ")

t1=threading.Thread(target=myfun,name="Child-1")
t2=threading.Thread(target=myfun,name="Child-2")
t1.start()
t2.start()
atc=threading.active_count()
print("Active Thread Count ",atc)

time.sleep(10)
atc=threading.active_count()
print("Active Thread Count : ",atc)
