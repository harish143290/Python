
#second.py
import sssitmodule
import time

for i in sssitmodule.lst_courses:
    time.sleep(1)
    print(i)

for k,d in sssitmodule.stu.items():
    time.sleep(1)
    print(k,d,sep='>>>')

sssitmodule.greetings()
