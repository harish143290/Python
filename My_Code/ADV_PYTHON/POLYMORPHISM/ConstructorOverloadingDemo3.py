


''' **x is nothingbut kwargs parameters
it can take N no.of keyword only arguments '''

import time
class Student:
    time.sleep(1)
    def __init__(self,**x):        
        for k,d in x.items():
            time.sleep(.2)
            print(k,d,sep=' <<<>>> ')
        print("=================")

'''calling'''
s1=Student(sno=10)
s2=Student(sno=102,sname="Ramesh")
s3=Student(sno=103,sname='Raj',scity='hyd')
s4=Student(sno=104,sname='Madhu',scity='kadapa',spin=500090)





        

    

        
