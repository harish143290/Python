
class Sample:
    def method1(self):
        print("Mtd-1 without arg")

    def method1(self,x):
        print("Mtd-1 with 1 args ",x)

'''Calling'''
s=Sample()
s.method1(123)
s.method1(222)
              
