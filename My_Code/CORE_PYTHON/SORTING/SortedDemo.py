

'''
  sorted(iterable,key=None,reverse=False) -> list
                iterable is list | tuple | set | str | dict ...
 
  list(iterable) -> list
  set(iterable) -> set
  tuple(iterable) -> tuple  
'''

lst=[40,50,30,20,10,4]
print("List : ",lst)
lst=sorted(lst)
print("After Sorting ",lst)
print("- "*30)

t=(50,40,30,60,70,20,3)
print("Tuple : ",t)
lst=sorted(t)
t=tuple(lst)
print("After sorting : ",t)
print("- "*30)

s={50,40,60,30,20,10,5}
print("Set : ",s)
lst=sorted(s)
print("After Sorting : ",lst)
print("- "*30)

st="aecbfdg"
print("Str : ",st)
lst=sorted(st)

'''S.join(iterable) -> str '''
st="".join(lst)
print("After Sorting : ",st)
print("- "*30)
