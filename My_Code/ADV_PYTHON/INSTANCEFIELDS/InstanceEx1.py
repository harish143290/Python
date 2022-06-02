
class Sample:
    def method1(self):
        x=10 #local
        self.y=20 #instance field
        print("local x val is : ",x) #10
        #print("y val is : ",y) NameError
        print("instance y val is : ",self.y) #20
        #print("instance z val is : ",self.z) AttributeError

'''calling '''
s=Sample()
s.method1()
