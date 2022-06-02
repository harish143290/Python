

'''Note : when there is not instance field
with specified name the priority is given
static variable if any variable is existed with that name '''

class Test:
    x=30
    def method1(self):
        x=10
        print("x val is : ",x)
        print("x val is : ",self.x)
        print("x val is : ",Test.x)

'''calling'''
t=Test()
t.method1()
    
