
class Sample:
    def method1(self):
        print("Mtd-1 of Sample")
        self.x=10
        print("x val is : ",self.x)

    def method2(self):
        print("Mtd-2 of Sample")
        self.x=20
        print("x val is : ",self.x)

'''calling'''
s=Sample()
s.method1()
s.method2()

        
