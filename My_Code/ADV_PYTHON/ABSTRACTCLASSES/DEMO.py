

''' Abstract methods and Abstract class '''

''' non abstract method '''
def method(self):
   print("Mtd-1 of Sample")

''' null body method acts as non abstract method
where as non abstract method not a null body mtd'''
def method2(self):
    pass

''' abstract method '''
@abstractmethod
def method3(self):
    pass

When do we use abstract methods ?
Ans : Whenever two or more sub classes required to
fullfil the same role through different implementation.

What is the class ?
   - collection of non abstract methods
   
class Sample:
    def method1(self):
        print("mtd-1 of Sample ")

    def method2(self):
        pass

What is the Abstract Class ?
  - collection of both abstract or non abstract methods
  - Creating an abstract class nothing but creating
  sub class of Class ABstractClass (ABC)
  - Both ABC and abstractmethod these are from abc
  module.

from abc import ABC,abstractmethod

class Sample(ABC):
    def method1(self):
        print("Mtd-1 of Sample")

    @abstractmethod
    def method2(self):
        pass




  








   
