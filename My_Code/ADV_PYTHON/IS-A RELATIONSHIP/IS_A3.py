
class Super:
    @staticmethod
    def method1():
        print("static mtd-1 of Super")

class Sub(Super):
    pass

'''calling '''
s=Sub()
s.method1()
Sub.method1()
