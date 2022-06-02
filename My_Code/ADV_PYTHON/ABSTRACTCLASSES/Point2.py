
from abc import ABC,abstractmethod

class Sample(ABC):
    def method1(self):
        print("method-1 of Sample")
        
    def method2(self):
        pass

''' calling '''
s=Sample()
'''
Note :
TypeError: Can't instantiate abstract class Sample
with abstract methods method2

Note : Abstract class without abstract method can be
instantiated. 
'''
