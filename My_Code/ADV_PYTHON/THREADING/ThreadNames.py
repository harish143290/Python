
''' Thread(target,args,name)
    name parameter used to set the name For thread '''

import threading

def myfun():
    for i in range(1,11):
        print("myfun ... ",i)

t1=threading.Thread(target=myfun)

'''get the name of thread object '''
tname=t1.getName()
print("Thread Name is : ",tname)
print("Thread Name is : ",t1.name)

''' t1.setName("Child") or '''
t1.name="Child"
tname=t1.getName()
print("Thread Name is : ",tname)
