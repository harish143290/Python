''' MyModule.py '''

class Employee:
    ''' Employee class is for Employee Salary Information '''
    def __init__(self):
        self.eno=101
        self.ename="Ramesh"

    def getEmployee(self):
        print("Eno is : ",self.eno)
        print("Ename is : ",self.ename)
        print("-"*20)


