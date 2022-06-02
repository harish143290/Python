import threading

def fun1():
    for i in range(1,11):
        print("Hello Dear ...",i)

def fun2():
    for i in range(20,31):
        print("Have a nice Day ... ",i)

''' calling '''
t1=threading.Thread(target=fun1)
t2=threading.Thread(target=fun2)
t1.start()
t2.start()

'''note: if u want make the function as thread then we
have to use Thread( ) -> Thread class object
                                      from threading module.

Thread(target,args,name) -> Thread
      target , args, name are keyword arguments

Thread execution will be starts by calling start()
from Thread class.'''




                                      

