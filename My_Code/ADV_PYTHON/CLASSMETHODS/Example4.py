class Sample:
    x=10
    def method1(self):
        self.y=20
        print("ins mtd-1 of Sample")
        print("instance field y is : ",self.y)
        print("static field x is : ",Sample.x)
        print("- "*20)

    @classmethod
    def method2(cls):
        print("cls mtd-2 of Sample ")
        print("static field x is : ",Sample.x)
        print("static field x is : ",cls.x)
        #print("inst field y is : ",self.y) NameError
        print("- "*20)
        
'''calling'''
s=Sample()
s.method1()
Sample.method2()




        

        
