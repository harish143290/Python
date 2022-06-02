
import threading
import time

def myfun():
    ct=threading.current_thread() 
    print(ct.getName(),"started its Execution ")
    time.sleep(10)
    print(ct.getName()," ends its Execution ")
    
'''mainthread'''
t1=threading.Thread(target=myfun,name="Cat")
t2=threading.Thread(target=myfun,name="Rat")
t3=threading.Thread(target=myfun,name="Man")

t1.start()
t2.start()
t3.start()

atc=threading.active_count()
print("No.of.Active Thread are : ",atc)

'''if u want to see all active threads details '''
lst=threading.enumerate()

for t in lst:
    time.sleep(.5)
    print(t.getName()," Its ident  : ",t.ident)










