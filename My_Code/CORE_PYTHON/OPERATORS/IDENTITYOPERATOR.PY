''' Identity operators are used to compare id's two objects
     is - returns True iff both object ids are same
                x is y --> id(x)==id(y)
                
     is not - returns True iff both object ids are not same
              x is not y ---> id(x)!=id(y) '''

x=10
print("Id(x) is ? : ",id(x))
y=x  #Ref.copy
print("Id(y) is ? : ",id(y))
print("ids of x and y are Same ? : ",x is y)

z=30
print("Id(z) is ? : ",id(z))
print("ids of x and z are Same ? : ",x is not z)









