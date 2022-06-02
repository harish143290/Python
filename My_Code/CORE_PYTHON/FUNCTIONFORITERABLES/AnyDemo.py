#any(iterable) -> bool
''' Note : any( ) returns false iff all the objects
in the collection | iterable is evaluated to
False

Non boolean false : 0 , 0.0 , 0+0j , None, "" ,[],(),{},set() '''

lst=[0,0.0,""]
print("List : ",lst)
b=any(lst)   
print("Result is : ",b)

#all  works as same as logical and
#any works as same as logical or



