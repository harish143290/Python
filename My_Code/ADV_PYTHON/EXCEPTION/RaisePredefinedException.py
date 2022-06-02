
''' accept acno from the user
    if the acno is +ve display valid acno
    if the acno is -ve raise ValueError '''

acno=int(input("Enter acno : "))

if acno>0:
    print("Valid acno ")
else:
    try:  
        raise ValueError()
    except ValueError:
        print("VE : Sorry Invalid acno ")
