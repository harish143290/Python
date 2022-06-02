
class TestIQ:
    x=10
    def method1(self):
        self.x=20
        print("x val is : ",self.x)
        print("x val is : ",TestIQ.x)

'''calling'''
t=TestIQ()
t.method1()
