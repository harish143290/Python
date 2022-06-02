''' varargs can also takes along with other
type of paramenter but in this case
varargs should be the last parameter.'''

import time
def myResult(name,*marks):
    time.sleep(1)
    print("Name is : ",name)
    print("Marks : ",marks)
    print("Total is : ",sum(marks))
    print("= "*20)

#calling
myResult("Ramesh",50,60,70,80,56,30)
'''
myResult(name="Sai",50,60,70,40,30,50)
Error  '''
    
    
