
import threading

cwt=threading.current_thread()
print("Type is : ",type(cwt))
tname=cwt.getName()
print("Thread name is : ",tname)

print("Thread name is : ",
      threading.current_thread().getName())
