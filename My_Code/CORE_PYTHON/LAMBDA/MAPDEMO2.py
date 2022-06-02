'''
map(func,*iterables) -> map object | iterable
list(iterable) -> list
tuple(iterable) -> tuple ...
'''

lst_rad=[1,2,3,4]
print("List_rad ",lst_rad)
t=tuple( map( lambda rad: 3.14*rad*rad , lst_rad) )
print("Result is : ",t)



