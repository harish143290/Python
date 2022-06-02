class Student:
    def __init__(self,no,name):
        print("Parameterized construc is invoked ")
        self.no=no
        self.name=name
        print("sno is : ", self.no)
        print("sname is : ", self.name)

    def getStudent(self):
        print("sno is : ",self.no)
        print("sname is : ",self.name)

'''calling'''
s=Student(101,"Kiran")
s.getStudent()
