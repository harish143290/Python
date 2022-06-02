
class Super:
    def __init__(self):
        self.__x=10

class Sub(Super):
    def getData(self):
        print("x val is : ",self.__x)

s=Sub()
s.getData()

