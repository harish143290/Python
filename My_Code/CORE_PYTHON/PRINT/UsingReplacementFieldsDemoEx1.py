
#print("replacement fields ".format(variables))

sno=101
sname="Ramesh"
scity="Hyd"

print("{}".format(sno))
print("sno is : {}".format(sno))
print("sno is :{} , sname is :{} and scity : {}".
      format(sno,sname,scity))

print("-"*30)
print("sno is :{}, sname is:{} and scity :{}".
      format(scity,sno,sname))
      #            0        1      2
      
print("-"*30)
print("sno is :{1}, sname is:{2} and scity :{0}".
      format(scity,sno,sname))

print("-"*30)
'''
print("sno is :{1}, sname is :{} and scity :{0}".
      format(scity,sno,sname))
ValueError: cannot switch from
manual field specification to automatic field numbering'''

print("sno is :{} , sname is :{}, city is :{} and {} is Manager".
      format(sno,sname,scity,sname))

print("sno is :{n} , sname is :{na}, scity is :{c} and {na} is manager".
      format(n=sno,na=sname,c=scity))





















      




