
class Super:
    @classmethod
    def method1(cls):
        print("Cls mtd-1 of Super")

class Sub:
    def method2(self):
        s=Super()
        s.method1()
        Super.method1()
        print("Instance mtd-2 of Sub ")

'''calling '''
s=Sub()
s.method2()
