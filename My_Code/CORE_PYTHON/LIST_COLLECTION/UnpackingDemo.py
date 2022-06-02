#       0    1                 2
lst=[10,"Ramesh","Hyd"]

no=lst[0]
name=lst[1]
city=lst[2]
print(no,name,city,sep=' <<>> ')

#Unpacking
a,b,c=lst
print(a,b,c,sep=' <<->> ')

#x,y=lst ValueError
x=lst #ref.copy
print("List lst : ",lst)
print("List x : ",x)

