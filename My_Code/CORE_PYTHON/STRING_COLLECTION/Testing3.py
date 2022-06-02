#input : given input is sssit
#input ( ) -> str
#str.replace(str,str) -> str
#str.upper( ) -> str

data=input("Enter any string : ") #sssit
db="Ss si  T   "

if data.replace(" ","").upper()==db.replace(" ","").upper():
    print("Valid User ")
else:
    print("Invalid user ")
