class MyLoginException(Exception):
    def __init__(self,msg):
        self.msg=msg

'''main_code '''
username=input("Enter Username : ")
password=input("Enter Password : ")

if username=="sssit" and password=="kphb":
    print("Valid User ")
else:
    try:
        raise MyLoginException('Invalid Username or password')
    
    except MyLoginException as e :
        print("Sorry Unable to continue....")
        print("Reason : ",e)
        



