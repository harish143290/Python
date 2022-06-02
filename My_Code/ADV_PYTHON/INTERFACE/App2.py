from abc import ABC,abstractmethod
class RBI(ABC):
    @abstractmethod
    def wd(self):
        pass

    @abstractmethod
    def be(self):
        pass

class SBI(RBI):
    def wd(self):
        print("WD From SBI")

    def be(self):
        print("BE From SBI ")

s=SBI()
s.wd()
s.be()

    
