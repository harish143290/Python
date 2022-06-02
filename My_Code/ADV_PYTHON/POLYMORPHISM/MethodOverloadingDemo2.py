import time

class Maths:    
    def myAdd(self,x=None,y=None,z=None):
        time.sleep(1)
        if x!=None and y!=None and z!=None:
            s=x+y+z
            print("Sum of three : ",s)
        elif x!=None and y!=None:
            s=x+y
            print("Sum of two : ",s)
        elif x!=None:
            s=x
            print("Sum of one : ",s)
        else:            
            s=0
            print("Sum is : ",s)
        
'''calling'''
m=Maths()
m.myAdd(10,20,30)
m.myAdd(10,20)
m.myAdd(10)
m.myAdd()
