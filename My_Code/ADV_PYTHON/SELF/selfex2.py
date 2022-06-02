
class Sample:
    def method1(self,x):
        print("Mtd-1 of Sample ")
        print("self :",self)
        print("x val is : ",x)
        print("- "*20)

    def method2(self,x,y,z):
        print("Mtd-2 of Sample ")
        print("x val is : ",x)
        print("y val is : ",y)
        print("z val is : ",z)

'''calling '''
s=Sample()
s.method1(10)
s.method2(20,30,40)
        
        
