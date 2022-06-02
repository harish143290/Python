import time

class Student:
    def setStudent(self):
        self.no=input("Enter no : ")
        self.name=input("Enter name : ")
        self.d=self.Dob()
        self.d.setDob()
        self.m=self.Marks()
        self.m.setMarks()

    def getStudent(self):
        print("no is : ",self.no)
        print("name is : ",self.name)
        print("-------------------------------")
        self.d.getDob()
        print("-------------------------------")
        self.m.getMarks()

    class Dob:
        def setDob(self):
            print("Enter Dob : ")
            self.dd=input("Enter DD : ")
            self.mm=input("Enter MM : ")
            self.yy=input("Enter YY : ")

        def getDob(self):
            print(f"Dob is : {self.dd}-{self.mm}-{self.yy}")            

    class Marks:
        def setMarks(self):
            print("Enter 3 sub marks with space ")
            self.marks=[int(i) for i in input().split()]

        def getMarks(self):
            print("Marks are : ")
            for i in self.marks:
                time.sleep(1)
                print(i)
            print("-----------------")
            print("total is : ",sum(self.marks)) #sum(iterable)

'''calling'''
s=Student()
s.setStudent()
s.getStudent( )
                


        
