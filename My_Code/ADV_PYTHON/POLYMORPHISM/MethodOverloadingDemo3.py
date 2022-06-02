
'''  sum(iterable) -> int '''

import time
class Sample:
    def myAdd(self,*x):
        time.sleep(1)
        print("type is : ",type(x))
        print("Data is : ",x)
        print("Sum is : ",sum(x))
        print("- "*20)

'''calling'''
s=Sample()
s.myAdd(10,20,30,40,50)
s.myAdd(10,20,30)
s.myAdd(10,20)
s.myAdd(10)
s.myAdd()








        


        
        
