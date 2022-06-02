import threading
def myfun():
    ct=threading.current_thread()
    print(ct.getName(),"started its execution ")
    mt.join()
    print(ct.getName(),"ends its execution ")    
    
''' Actual logic '''
mt=threading.current_thread() #mainthread
t1=threading.Thread(target=myfun,name="Child")
t1.start()

print(mt.getName(),"Started its execution ")
t1.join()
print(mt.getName(),"ends its execution ")

