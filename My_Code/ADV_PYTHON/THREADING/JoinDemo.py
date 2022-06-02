import time
import threading

class Cat(threading.Thread):
    def run(self):
        for i in range(1,11):
            time.sleep(2)
            print("Cat ... ",i)

class Rat(threading.Thread):
    def run(self):
        for i in range(20,31):
            print("Rat >>> ",i)

c=Cat()
r=Rat()
c.start()
c.join()
r.start()

