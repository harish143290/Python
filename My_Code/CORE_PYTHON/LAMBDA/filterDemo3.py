

'''
filter(function or None,iterable) -> filter object | iterable

list(iterable) -> list
tuple(iterable) -> tuple
set(iterable) -> set

'''

lst=["anu","srija","cnu","ram","Ramesh","suresh"]
print("List :",lst)

lstr=list( filter( lambda x: x[0]=='r', lst ) )
print("Result is : ",lstr)

lstr2=list( filter( lambda x: x[0]=='r' or x[0]=='R' , lst) )
print("Result is : ",lstr2)

lstr3=list( filter( lambda x : x[0] in ['r','R'] ,lst))
print("Result is : ",lstr3)

lstr4=list( filter(lambda x : x.startswith('r') or x.startswith('R'),lst) )
print("Result is : ",lstr4)
















