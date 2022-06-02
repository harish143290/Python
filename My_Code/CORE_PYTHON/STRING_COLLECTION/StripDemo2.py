
#S.lstrip([chars]) -> str
#S.rstrip([chars]) -> str
#S.strip([chars]) -> str

''' lstrip( ) returns str by erasing the specified char(s)
from the left of the string object. if we ignore to specify
char(s) then PVM will erase empty spaces if existed @
left side of string ||y rstrip() it will perform right side
strip( ) means either of sides '''

fn=input("Enter First Name : ")
ln=input("Enter Last Name : ")
f=fn.strip()
l=ln.strip()
fln=f+l
print("Result is : ",fln)

