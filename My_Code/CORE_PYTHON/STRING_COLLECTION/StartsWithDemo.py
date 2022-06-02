
#input(prompt=None) -> str
#S.startswith(chars) -> bool
#S.endswith(chars) -> bool

main=input("Enter main string :  ") #hello dear friend
sub=input("Enter sub string : ") # hi

if main.startswith(sub):
    print(main," starts with ",sub)
else:
    print(main," not starts with ",sub)
    

