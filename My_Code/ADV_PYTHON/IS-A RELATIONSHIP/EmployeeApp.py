import time

class PersonInfo:
    def setPerson(self):
        self.no=input("Enter no : ")
        self.name=input("Enter name : ")

    def getPerson(self):
        print("no is : ",self.no)
        print("name is : ",self.name)
        print("--------------------------------")

class OffInfo(PersonInfo):
    def setOinfo(self):
        self.job=input("Enter job : ")
        self.salary=int(input("Enter Salary : "))

    def getOinfo(self):
        print("job is : ",self.job)
        print("Salary is : ",self.salary)
        print("------------------------------------")

class Employee(OffInfo):
    def setEmployee(self):
        self.setPerson()
        self.setOinfo()

    def getNetSalary(self):
        self.hra=(self.salary*10)/100
        self.ta=(self.salary*5)/100
        self.netsal=self.salary+self.hra+self.ta
        print("HRA is  : ",self.hra)
        print("TA  is    : ",self.ta)
        print("Netsal  : ",self.netsal)
        print("-------------------------------------------")

    def getEmployee(self):
        time.sleep(1)
        self.getPerson()
        time.sleep(1)
        self.getOinfo()
        time.sleep(1)
        self.getNetSalary()
        
'''calling '''
e=Employee()
e.setEmployee()
e.getEmployee()
        

