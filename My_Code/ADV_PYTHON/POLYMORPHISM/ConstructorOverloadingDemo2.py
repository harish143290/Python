''' len(iterable) -> int '''

import time

class Sample:
    def __init__(self,*x):
        time.sleep(1)
        print("constructor with ",len(x),"arguments ")

''' calling '''
s=Sample()
s1=Sample(10,20)
s2=Sample(10,20,30,40)
s3=Sample(10,20,30,40,50,60,70)

        
        
