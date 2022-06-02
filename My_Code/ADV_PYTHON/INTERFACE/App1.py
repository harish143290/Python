
from abc import ABC,abstractmethod

'''abstract class 
class Sample(ABC):
    def method1(self):
        print("mtd-1 of Sample")

    @abstractmethod
    def method2(self):
        pass
'''

''' its pure abstract class called an interface '''
class Testing(ABC):
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass


'''
Note: abstract method is nothing a method which is
not having any body | logic or implementation

2.By calling abstract methods can do nothing thus
abstract methods also known as 'do nothing' methods

3. if any class [abstract class or interface]
     existed with abstract methods then thoses are
     not allowed to create an object.
'''






    



    
