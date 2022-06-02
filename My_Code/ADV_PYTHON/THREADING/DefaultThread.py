
import threading

def myfun():
    for i in range(1,11):
        print("MyFun ... ",i)

''' calling '''
t1=threading.Thread(target=myfun)
t1.start()

'''mainlogic'''
for i in range(20,31):
    print("Main Thread ... ",i)
