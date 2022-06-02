


import time

def myStudent(**stu):
    time.sleep(1)
    print("Student Datails ")

    for k,d in stu.items():
        time.sleep(.3)
        print(k,d,sep=' ----> ')

    print("- "*20)

#calling
myStudent(sno=101)
myStudent(sno=102,sname='Ramesh')
myStudent(sno=103,sname='Roja',scity='hyd')
myStudent( )
          
