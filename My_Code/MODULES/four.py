''' Based on the application req
    we can avoid to write lengthy module
    names by providing alias names to modules

    Syn: import <modulename> as <aliasname>
    Syn: import module1,module2,......
    
    '''
#four.py

import sssitmodule as sm,time as t

print("List of courses ")
for i in sm.lst_courses:
    t.sleep(1)
    print(i)
print("- "*30)

print("Student Details ")
for k,d in sm.stu.items():
    t.sleep(1)
    print(k,d,sep='<<<>>>')

print("- "*30)
sm.greetings()

