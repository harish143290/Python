#all(iterable) -> bool
''' Note : all( ) returns Ture iff all the objects
in the collection | iterable is evaluated to
True

Non boolean false : 0 , 0.0 , 0+0j , None, "" ,[],(),{},set() '''

lst=[10,2.2,"shashi"]
print("List : ",lst)
b=all(lst)
print("Result is : ",b)



