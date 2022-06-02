class Student:
    course="Python" #static variable

    def setStudent(self):
        self.no=input("Enter Sno : ")
        self.name=input("Enter sname : ")

    def getStudent(self):
        print("Sno is : ",self.no)
        print("Sname is : ",self.name)
        print("Course is : ",Student.course)
        print("- "*20)

'''calling'''
s1=Student()
s1.setStudent( )
s1.getStudent( )

s2=Student()
s2.setStudent( )
s2.getStudent( )


