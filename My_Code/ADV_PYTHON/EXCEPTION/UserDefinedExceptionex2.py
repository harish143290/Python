import re

class MobileException(Exception):
    def __init__(self,msg):
        self.msg=msg

''' main_code '''
data=input("Enter Mobile number  :  ") 
m=re.fullmatch("[7-9][0-9]{9}",data)

if m!=None:
    print("Valid Mobile Number")
else:
    try:
        raise MobileException('Invalid Mobile Number')
    except MobileException as me:
        print("Sorry unable to continue....")
        print("Reason is : ",me)
        
