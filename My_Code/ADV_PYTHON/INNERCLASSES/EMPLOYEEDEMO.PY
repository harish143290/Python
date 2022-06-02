class Employee:
    def setEmployee(self):
        self.eno=input("Enter Eno : ")
        self.name=input("Enter Ename : ")

    def getEmployee(self):
        print("Eno is : ",self.eno)
        print("Ename is : ",self.name)
        print("-------------------------------")

    class Doj:
        def setDoj(self):
            print("Enter Doj ")
            self.dd=input("Enter DD :")
            self.mm=input("Enter MM : ")
            self.yy=input("Enter YY : ")

        def getDoj(self):
            print("Doj is :{}/{}/{}".format(self.dd,self.mm,self.yy))
            print(f"Doj is :{self.dd}/{self.mm}/{self.yy}")
            
'''Calling'''
e=Employee()
e.setEmployee()

d=e.Doj()
d.setDoj( )

e.getEmployee()
d.getDoj()



            
