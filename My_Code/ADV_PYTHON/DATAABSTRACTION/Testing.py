class Super:
    def __init__(self):
        self.__x=10
        self._y=20
        self.z=30

    def getDataSuper(self):
        print("From sub class ")
        print("Private x : ",self.__x)
        print("protected y : ",self._y)
        print("public z : ",self.z)

class Sub(Super):
    def getDataSub(self):        
        print("From sub class ")
        #print("Private x : ",self.__x)
        print("protected y : ",self._y)
        print("public z : ",self.z)

s=Sub()
s.getDataSub()

print("From Outside : ")
'''print("private x : ",s.__x)  Error'''
print("private x : ",s._Super__x)
print("protected y : ",s._y)
print("public z : ",s.z)





