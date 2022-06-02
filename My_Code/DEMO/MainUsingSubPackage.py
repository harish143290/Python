


'''
import mainpkg7am.subpkg7am.sssitmodule
import time

for k,d in mainpkg7am.subpkg7am.sssitmodule.courses.items():
    time.sleep(1)
    print(k,d,sep=' >>> ')

'''

from mainpkg7am.subpkg7am.sssitmodule import *
from time import sleep

for k,d in courses.items():
    sleep(1)
    print("Course Name is : ",k)
    print("Fee : ",d)
    print("- "*20)


    
