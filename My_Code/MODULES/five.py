
'''Based on the application req
we can also import only req members
from the module by using from keyword

Syn: from <modulename> import <members(s)>

Note: if any members from module is imported by using
from keyword then doesn't req use the modulename to
use those members.
'''
from sssitmodule import stu,greetings
from sssitmodule  import *
from time import sleep

for k,d in stu.items():
    sleep(.2)
    print(k,d,sep='<<<>>>')
print("- "*30)

greetings()
print("- "*30)

print("List of courses ")
print(lst_courses)



    
    
