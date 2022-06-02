
'''
   input( ) -> str
   str.split([chars]) -> list   
'''

data=input("Enter 3 number with space ") #"10 20 30"
lst=data.split( ) #['10','20','30'] split methof splits a string into a list
print(lst)
print(type(lst[1]))
lst2=[int(i) for i in lst]
print(lst2)
print("- "*30)

data=input("Enter 3 numbers with space ")
lst=[int(i) for i in data.split() ]
print(lst)
print("- "*30)

x,y,z=[int(i) for i in input("enter 3 no").split( )]
print(x,y,z,sep='<<>>')






    
