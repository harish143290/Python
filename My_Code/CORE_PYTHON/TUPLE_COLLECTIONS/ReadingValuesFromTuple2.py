#       0   1    2                3                 4             5
t=(10,2.2,"Shashi",(10+20j),"Kumar",10)
print("Data is : ",t)

#len(iterable) -> int
ni=len(t)
print("No.of.Items : ",ni)

#Reading values From tuple using while
import time

index=0
while index<len(t):
    time.sleep(1)
    print(t[index])
    index=index+1
print("- "*20)

#Reading values From tuple using for
for i in t:
    time.sleep(1)
    print(i)

''' Note: List is mutable, where as tuple is immutable
thus append( ), insert( ), extend( ), copy( ), pop( ),
remove( ), clear( ), reverse( ) are not supported

but we can perform index( ) and count( )
on the tuple collection '''






    





    

