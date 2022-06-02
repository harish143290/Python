#input(prompt=None) -> str
'''Accept String from the user findout nc,
ns,nd,nsp,nsy,tnl '''

import time
nc=ns=nd=nsy=nsp=tnl=0

data=input("Enter u r data : ")

for i in data:
    time.sleep(.2)
    if i.isupper():
        nc=nc+1
    elif i.islower():
        ns=ns+1
    elif i.isdigit():
        nd=nd+1
    elif i.isspace():
        nsp=nsp+1
    else:
        nsy=nsy+1

print("NC is : ",nc)
print("NS is : ",ns)
print("ND is : ",nd)
print("NSP is : ",nsp)
print("NSY is : ",nsy)
print("TNL is : ",len(data))



        

