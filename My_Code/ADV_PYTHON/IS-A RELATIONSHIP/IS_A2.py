
class Super:
    @classmethod
    def method1(cls):
        print("cls mtd-1 of Super")

class Sub(Super):
    pass

'''calling '''
s=Sub()
s.method1()
Sub.method1()





    
