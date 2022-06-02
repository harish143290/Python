class Sample:
    def method1(self):
        print("Instanct mtd-1 of Sample")
        print("self : \n",self)
        print("- "*30)

    @classmethod
    def method2(cls):
        print("Mtd-2 of Sample")
        print("cls : \n",cls)
        print("- "*30)

'''calling'''
s=Sample()
s.method1()
Sample.method2()
s.method2()
