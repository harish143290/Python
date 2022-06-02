class Student:
    def setStudent(self):
        '''
        self.m1=int(input("Enter M1 : "))
        self.m2=int(input("Enter M2 : "))
        self.m3=int(input("Enter M3 : "))  '''
        
        print("Enter 3 sub marks ")
        self.m1,self.m2,self.m3=int(input()),int(input()),int(input())
        

    def findResult(self):
        if self.m1>34 and self.m2>34 and self.m3>34:
            return True
        else:
            return False

'''calling'''
s=Student( )
s.setStudent( )
if  s.findResult( ) :
    print("Student is Pass")
else:
    print("Student is Fail")



