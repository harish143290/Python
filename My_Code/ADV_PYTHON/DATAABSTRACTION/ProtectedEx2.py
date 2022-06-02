
class Super:
    def __init__(self):
        self._x=10

class Sub(Super):
    def getData(self):
        print("sub class x val is : ",self._x)

'''calling'''
s=Sub()
s.getData()
