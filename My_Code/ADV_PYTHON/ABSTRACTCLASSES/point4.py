
from abc import ABC,abstractmethod

class Test(ABC):
    def method1(self):
        print("method-1 of Sample")

    @abstractmethod    
    def method2(self):
        pass

class Testing(Test):
    def method2(self):
        print("OR mtd-2 of Test ")

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

Note 4:
if any class in inherited by abstract class with abstract
methods then we must override all the abstract method
of its super class, otherwise the sub class acts an
abstract class

Note 5:
creating an object for an abstract class nothing but
creating an object for any of its concreate class.

Note 6:
concreate class is a class which is overridden all
abstract method of its super class.
'''
