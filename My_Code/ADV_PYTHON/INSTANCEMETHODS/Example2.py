
class Sample:
    def method1(self):
        print("Instance mtd-1 of Sample")

    def method2(self):
        self.method1() #here self ref current class.
        print("Instance mtd-2 of Sample")

'''calling'''
s=Sample()
s.method2()