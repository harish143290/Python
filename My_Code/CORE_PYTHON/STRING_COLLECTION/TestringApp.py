#input(prompt=None) -> str
#S.isalnum( ) -> bool

import time

data=input("Enter any string : ")
nc=ns=nd=0

if data.isalnum():
    print("Yes given data is alnum ")
    for i in data:
        time.sleep(.2)
        if i.isupper():
            nc=nc+1
        elif i.islower():
            ns=ns+1
        elif i.isdigit():
            nd=nd+1

    print("No.of.Cap : ",nc)
    print("No.of.Small : ",ns)
    print("No.of.Digits : ",nd)
    
else:
    print("Sorry given data is not alnum ")
