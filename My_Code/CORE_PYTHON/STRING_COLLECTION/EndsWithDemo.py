
#input(prompt=None) -> str
#S.startswith(chars) -> bool
#S.endswith(chars) -> bool

main=input("Enter main string :  ") #hello dear friend
sub=input("Enter sub string : ") # hi

if main.endswith(sub):
    print(main," ends with ",sub)
else:
    print(main," not ends with ",sub)
    

