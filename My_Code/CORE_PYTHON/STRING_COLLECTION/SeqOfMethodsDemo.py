
#input(prompt=None) -> str
#S.upper( ) -> str
#S.startswith(char) -> bool

data=input("Enter Data : ")
uc=data.upper( )

print("Result is : ",uc)

#App-2
if input("Enter Data : ").upper( ).startswith('HI'):
    print("Given String is starts with Hi")
else:
    print("Given String is not starts with Hi")
