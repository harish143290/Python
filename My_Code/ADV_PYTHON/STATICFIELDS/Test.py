
class Test:
    x=10
    def method1(self):
        # print("x val is : ",x)NameError
        print("x val is : ",self.x)
        print("x val is : ",Test.x)

'''calling'''
t=Test()
t.method1()
    
