
'''
from functools module
reduce(function,sequence) -> value
'''

import functools

lst=[1,2,3,4,5]
r=functools.reduce( lambda x,y: x+y , lst)
print("Result is : ",r)

f=functools.reduce( lambda x,y : x*y , [1,2,3,4,5,6] )
print("Fact is : ",f)

