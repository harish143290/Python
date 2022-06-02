# sssit | SSSIT | SssiT               kphb
#username            and        password
#usernames are not case sensitive where as
#password are  case sensitive

un=input("Enter user name : ") #sssit
pw=input("Enter password : ")  #kphb
dbun="SsSiT"
dbpw="kphb"
    
if un.upper()==dbun.upper() and pw==dbpw:
    print("Valid User ")
else:
    print("Invalid User ")
