lst1=[]
print("Type is : ",type(lst1))
print("List : ",lst1)
print("- "*30)

lst2=[10,2.2,(10+20j),None,10,"Shashi","Ramesh"]
print("Type is : ",type(lst2))
print("List : ",lst2)
print("- "*30)

#list( ) -> list
lst3=list( )
print("Type is : ",type(lst3))
print("List : ",lst3)
print("- "*30)

#list(iterable) -> list
#iterable -> str | list | set | tuple | dict | range...
t=(10,20,30,40)
print("Type is : ",type(t))
print("Tuple Objects are : ",t)
lst4=list(t)
print("List : ",lst4)

#String to list covertion
s="welcome"
lst5=list(s)
print("List : ",lst5)

#dict to list collection
stu={"sno":101,"sname":"ramesh"}
print("Dict : ",stu)
lst6=list(stu)
print("List : ",lst6)

#range(start,stop[,step]) -> range object | iterable
#Converting range to list 
r=range(1,11)
lst7=list(r)
print("list : ",lst7)

#S.split([chars]) -> list
s="have a nice day"
lst8=s.split()
print("List : ",lst8)













































