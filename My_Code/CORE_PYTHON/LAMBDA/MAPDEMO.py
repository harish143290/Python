'''
map(func,*iterables) -> map object | iterable
'''

lst=[1,2,3]
lsts=[]

'''
def sq(x):
    r=x*x
    return r

for i in lst:
    a=sq(i)
    lsts.append(a)
print("Result is : ",lsts) '''

''' App-2
m=map(sq,lst)
print("Type is : ",type(m))
print("Map object : ",m)
#list(iterable) -> list
lsts=list(m)
print("Result is : ",lsts)
'''

m=map(lambda x: x*x,lst)
lst2=list(m)
print("Result is : ",lst2)

lst3=list( map(lambda x:x*x, lst) )
print("Result is : ",lst3)






