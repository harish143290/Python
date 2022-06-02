#input(prompt=None) -> str
'''Accept String from the user findout nc,
ns,nd,nsp,nsy,tnl
  A TO Z : 65 to 90
  a to z : 97 to 122
  0 to 9 : 48 to 57
  Space bar : 32 '''

import time
nc=ns=nd=nsy=nsp=tnl=0

data=input("Enter u r data : ")

for i in data:
    if ord(i)>=65 and ord(i)<=90:
        nc=nc+1
    elif ord(i)>=97 and ord(i)<=122:
        ns=ns+1
    elif ord(i)>=48 and ord(i)<=57:
        nd=nd+1
    elif ord(i)==32:
        nsp=nsp+1
    else:
        nsy=nsy+1

print("NC : ",nc)
print("NS : ",ns)
print("ND : ",nd)
print("NSP : ",nsp)
print("NSY : ",nsy)





        
        

