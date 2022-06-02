class Sample:
    def method1(self):
        print("Mtd-1 of Sample")
        x=10
        self.y=20
        print("local x val is : ",x)
        print("instance y val is : ",self.y)
        print("- "*20)

    def method2(self):
        self.method1()
        print("Mtd-2 of Sample ")
        #print("x val is : ",x) NE
        print("Instance y val is : ",self.y)
        print("- "*20)
        
'''calling'''
s=Sample()
s.method1()
s.method2()
print("From outside of the class ")
# print("y val is : ",self.y) NameError
print("y val is : ",s.y)




