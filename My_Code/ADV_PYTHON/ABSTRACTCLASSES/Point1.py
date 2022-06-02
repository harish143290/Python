
from abc import ABC,abstractmethod

class Sample(ABC):
    def method1(self):
        print("method-1 of Sample")

    @abstractmethod
    def method2(self):
        pass

''' calling '''
s=Sample()
'''TypeError: Can't instantiate abstract class Sample
with abstract methods method2  '''
