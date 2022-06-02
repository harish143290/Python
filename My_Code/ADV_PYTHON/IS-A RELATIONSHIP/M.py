class PInfo:
    def setPerson(self):
        self.no=input("Enter no : ")
        self.name=input("Enter name : ")

    def getPerson(self):
        print("no is : ",self.no)
        print("name is : ",self.name)
        print("--------------------------------")

class Student(PInfo):
    def setStudent(self):
        self.setPerson()
        self.course=input("Enter course : ")
        self.fee=int( input("Enter Fee : ") )
        self.paid=int(input("Enter Paid : "))
        self.due=self.fee-self.paid

    def getStudent(self):
        self.getPerson()
        print("course is : ",self.course)
        print("Fee is : ",self.fee)
        print("Paid is : ",self.paid)
        print("-----------------------------------")
        print("Due is : ",self.due)

class Employee(PInfo):
    def setEmployee(self):
        self.setPerson()
        self.job=input("Enter job : ")
        self.salary=int(input("Enter salary : "))
        self.asal=self.salary*12

    def getEmployee(self):
        self.getPerson()
        print("Job is : ",self.job)
        print("salary is : ",self.salary)
        print("Anual Sal : ",self.asal)
                      

'''calling'''
s=Student()
s.setStudent()
print("Student Details....")
s.getStudent()

print("\n\n")
e=Employee()
e.setEmployee()
print("Employee Details ....")
e.getEmployee()
        




        
        
                     
