
class Super:
    def __init__(self):
        self.x=10

    def getData(self):
        print("x val is : ",self.x)

''' calling '''
s=Super( )
s.getData()
print("From outside of the class ")
print("x val is : ",s.x)
