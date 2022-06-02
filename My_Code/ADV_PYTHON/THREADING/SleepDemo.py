import threading
import time

class Cat(threading.Thread):
    def run(self):
        for i in range(1,11):
            print("Cat ... ",i)

class Rat(threading.Thread):
    def run(self):
        for i in range(20,31):
            print("Rat >>> ",i)

''' mainlogic'''
c=Cat()
r=Rat()
c.start()

for i in range(40,51):
    print("Main <<< ",i)
 
time.sleep(5)
r.start()





                  
