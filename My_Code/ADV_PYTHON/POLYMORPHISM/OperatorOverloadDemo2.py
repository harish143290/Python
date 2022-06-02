class Employee:
    def __init__(self):
        self.name=input("Enter Ename : ")
        self.salpd=int(input("Enter Salary Per Day : "))

    def __mul__(self,other):
        return self.salpd*other.dayswd

class TimeSheet:
    def __init__(self):
        self.dayswd=int(input("Enter Days worked : "))

    def __mul__(self,other):
        return self.dayswd*other.salpd
        
e=Employee()
t=TimeSheet()
ns=t*e  # t.__mul__(e)
print("Netsalary is : ",ns)
