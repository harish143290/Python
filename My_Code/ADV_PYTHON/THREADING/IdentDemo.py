
import threading

def myfun():
    for i in range(1,11):
        print("myfun ... ",i)

t1=threading.Thread(target=myfun)
t1.start()
print("Thread Identity ? : ",t1.ident)
