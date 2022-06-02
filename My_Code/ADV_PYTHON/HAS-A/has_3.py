
class Super:
    @staticmethod
    def method1():
        print("static mtd-1 of Super")

class Sub:
    def method2(self):
        s=Super()
        s.method1()
        Super.method1()
        print("Mtd-2 of Sub")

'''calling'''
s=Sub()
s.method2()
