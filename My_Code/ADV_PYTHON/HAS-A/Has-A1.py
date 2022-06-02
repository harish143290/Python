
class Super:
    def method1(self):
        print("Ins mtd-1 of Super")

class Sub:
    def method2(self):
        s=Super( )
        s.method1()
        print("Ins mtd-2 of Sub")

'''calling'''
s=Sub()
s.method2()
