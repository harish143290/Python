'''Note: the first argument of any method
will work as self only. '''

class Sample:
    def method1(shashi,*x):
        print("Mtd-1 of Sample")
        print("shashi : \n ",shashi)

    def method2(self):
        print("Mtd-2 of Sample")
        print("self : \n ",self)

    def method3(x,y,z):
        print("Mtd-3 of Sample ")
        print("x : \n ",x)
        print("y val is : ",y)
        print("z val is : ",z)

'''calling '''
s=Sample()
s.method1()
s.method2()
s.method3(10,20)
