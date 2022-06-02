
class Super:
    def __init__(self):
        self.x=10

class Sub(Super):
    def getData(self):
        print("sub x val is : ",self.x)

''' calling '''
s=Sub( )
s.getData()

print("From outside of the class ")
print("x val is : ",s.x)
