
#S.lstrip([chars]) -> str
#S.rstrip([chars]) -> str
#S.strip([chars]) -> str

''' lstrip( ) returns str by erasing the specified char(s)
from the left of the string object. if we ignore to specify
char(s) then PVM will erase empty spaces if existed @
left side of string ||y rstrip() it will perform right side
strip( ) means either of sides '''

s="xysssit"
print("Data is : ",s)
s2=s.lstrip('xy')
print("Result is : ",s2)
print("- "*20)

s="sssitxy"
print("Data is : ",s)
s2=s.rstrip('xy')
print("Result is : ",s2)
print("- "*20)

s='xxsssitxx'
print("Data is : ",s)
s2=s.strip('xx')
print("Result is : ",s2)














