
from abc import ABC,abstractmethod

class Test(ABC):
    def method1(self):
        print("method-1 of Sample")

    @abstractmethod    
    def method2(self):
        pass

class Testing(Test):
    pass

''' calling '''
t=Testing()

'''
Note :
TypeError: Can't instantiate abstract class Sample
with abstract methods method2

Note : Abstract class without abstract method can be
instantiated.

Note 3:
If any class is inherited by abstract class with abstract
method then that sub class also acts an abstract class.
'''
