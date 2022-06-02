

'''
filter(function or None,iterable) -> filter object | iterable

list(iterable) -> list
tuple(iterable) -> tuple
set(iterable) -> set

'''

lst=["anu","srija","cnu","ram","ramesh","suresh"]
print("List :",lst)

lst2=list( filter( lambda x: len(x)==3 , lst) )
print("names with 3 char : ",lst2)




