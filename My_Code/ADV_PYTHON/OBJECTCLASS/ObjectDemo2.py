import MyModule
e=MyModule.Employee()
print(dir(e))
print("ClsName of ",e.__class__)
print("Module Name is : ",e.__module__)
print("Doc_String is : \n ",e.__doc__)

''' e.job='Manager'  For Adding new instance field'''
e.__setattr__('job','Manager')
e.__setattr__('salary','9999$')

''' For reading the value from an instance field '''
job_title=e.job
print("Job_Title is : ",job_title)

salary=e.__getattribute__('salary')
print("Salary is : ",salary)

''' For deleting instance field '''
del e.salary

''' For Reading Fields and their values '''
d=e.__dict__
print("Fields : ",d)

''' salary=e.salary AttributeError '''
e.__delattr__('job')
d=e.__dict__
print("Fields : ",d)

e.__delattr__('ename')
print("Fields : ",d)









