#       0   1    2                3                 4             5
t1=(10,2.2,"Shashi",(10+20j),"Kumar",10)
print("Data is : ",t1)

#indexing
print("3rd Object : ",t1[2])
print("Last Object : ",t1[5])

#Slicing [start : end : step ]
print("First 3 Objects : ",t1[0:3:1])
print("Last 3 Objects : ",t1[3:6:1])

#unpacking
t=(10,"Shashi","Hyd")
no,na,ci=t
print(no,na,ci,sep=' ---> ')
print("- "*30)

#unpacking using slicing
t=(10,"shashi","hyd",40,50,60)
m1,m2,m3=t[3:6:1]
print(m1,m2,m3)
















