
class Sample:
    def __init__(self):
        self.__x=10

    def getData(self):
        print("x val is : ",self.__x)

''' calling '''
s=Sample()
s.getData()
print("From outside of the class ")
print("private x val is : ",s.__x)
