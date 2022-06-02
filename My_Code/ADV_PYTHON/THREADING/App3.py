
import threading

class Cat(threading.Thread):
    def run(self):
        for i in range(1,11):
            print("Cat ... ",i)

class Rat(threading.Thread):
    def run(self):
        for i in range(20,31):
            print("Rat ... : ",i)

'''calling'''
c=Cat()
r=Rat()
#c.run()
c.start()

#r.run()
r.start()




    
    
