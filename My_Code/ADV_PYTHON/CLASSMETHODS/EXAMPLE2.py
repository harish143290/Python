
class Sample:
    @classmethod
    def method1(cls):
        print("cls mtd-1 of Sample")

    def method2(self):
        self.method1()
        Sample.method1()
        print("ins mtd-2 of Sample ")

'''calling '''
s=Sample()
s.method2()


        
