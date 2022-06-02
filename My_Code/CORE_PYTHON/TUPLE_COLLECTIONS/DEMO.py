t1=()
print("type is : ",type(t1))
print("Data is : ",t1)
print("-"*30)

t2=(10,2.2,(10+20j),"shashi",10,None)
print("Type is : ",type(t2))
print("Data is : ",t2)
print("- "*30)

#tuple( ) -> tuple object
t3=tuple()
print("type is : ",type(t3))
print("Data is : ",t3)
print("- "*30)

#tuple(iterable) -> tuple object
#converting string to tuple
s="welcome"
t4=tuple(s)
print("type is : ",type(t4))
print("Data is : ",t4)
print("- "*30)

#converting list to tuple
lst=[10,2.2,"shashi",None,"Python"]
t5=tuple(lst)
print("type is : ",type(t5))
print("Data is : ",t5)
print("- "*30)

#packing
t6=10,20,3.3,"shashi",30
print("Type is : ",type(t6))
print("Data is : ",t6)
print("- "*30)

#Creating tuple using only object
t7=(2.2,)
print("Type is : ",type(t7))
print("Data is : ",t7)






























