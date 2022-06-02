class Student:
    def __init__(self):
        self.sname=input("Enter sname : ")
        self.scity=input("Enter Scity : ")
        self.sage=int(input("Enter Sage : "))

    def getStudent(self):
        print("---------------------------------")
        print("sname is : ",self.sname)
        print("scity is : ",self.scity)
        print("sage is : ",self.sage)
        print("---------------------------------")

    def __lt__(self,other):
        if self.sage<other.sage:
            return True
        else:
            return False       

s1=Student()
s2=Student()
if s1<s2:
    s1.getStudent( )
else:
    s2.getStudent( )
