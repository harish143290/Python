

'''
filter(function or None,iterable) -> filter object | iterable

list(iterable) -> list
tuple(iterable) -> tuple
set(iterable) -> set

'''

lst=["anu","","cnu",0,"Ramesh","suresh","sai",0.0,"","raj"]
print("List :",lst)

lst2=list( filter(None,lst) )
print("Result is : ",lst2)

