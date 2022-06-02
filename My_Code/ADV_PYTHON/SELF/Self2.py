
class Sample:
    def method1(self):
        print("From mtd-1")
        print("self : \n  ",self)
        print("-"*20)

    def method2(self):
        print("From mtd-2")
        print("self : \n",self)
        print("- "*20)

'''Calling'''
s=Sample()
print("From Outside of the class")
print("hcode of s : \n",s)
print("- "*20)
s.method1()
s.method2()

        
