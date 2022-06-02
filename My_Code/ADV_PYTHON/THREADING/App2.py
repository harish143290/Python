import threading

class Kiran:
    def method1(self):
        for i in range(1,11):
            print("Iam kiran ... ",i)

class Shashi:
    def method2(self):
        for i in range(20,31):
            print("Iam Shashi ... ",i)

k=Kiran()
s=Shashi()
t1=threading.Thread(target=k.method1)
t2=threading.Thread(target=s.method2)
t1.start( )
t2.start( ) 

''' if u want make any method as thread then we have to
use Thread( ) from threading module
        Thread(target,args,name) -> Thread '''


        
