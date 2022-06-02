

'''
filter(function or None,iterable) -> filter object | iterable

list(iterable) -> list
tuple(iterable) -> tuple
set(iterable) -> set

'''

lst=[1,2,3,4,5]
f=filter( lambda x: x%2==0 , lst)
print("Type is : ",type(f))
print("Filter Object : ",f)
lst2=list(f)
print("Result is : ",lst2)


