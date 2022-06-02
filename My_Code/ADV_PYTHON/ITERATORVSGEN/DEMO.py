'''
Iterators
   Looking statement :
         Whenever u want execute any statement
         or group of statement(s) again and again then
         we have to work with looping statement(s) |
         control statement | iterators

    iterable(s) nothing collections where we can read
    one by one object from that collection.
            Eg:  str | list | tuple | set | frozenset | dict |
            OrderedDict | file | cursor | dict_keys |
            dict_values | dict_items .......

import time
lst=[10,20,30,40,50]

for i in lst:
    time.sleep(1)
    print(i)


x=100
for i in x:
    time.sleep(.1)
    print(i)


Note: reading the values from list collections possible
bcoz list is an iterable,where as reading values from
int is not possiable bcoz int type is not iterable

In the Python For Every Data type is class.

if any class which is overridden with the following
methods then that classes are acts as an iterable
object.

__iter__(self)
    it will return current class object
    
__next__(self)
   it should return next item from the iterable collection.
   whenever collection is complited in printing
   all the values then __next__(self) method should
   raise StopIteration

s="shashi"
for i in s:
    time.sleep(.2)
    print(i)

for i in range(1,11):
    time.sleep(.2)
    print(i)
'''

lst=[i for i in range(1,11)]
print("Type is : ",type(lst))
print("Result is : ",lst)
print("- "*20)

t=(i for i in range(1,11))
print("Type is : ",type(t))
print("Result is : ",t)

import time
for i in t:
    time.sleep(1)
    print(i)

'''generator is an alternative way for creating iterable
objects.but iterable collections are taking more space
than generator.

generator are faster in execution rather iterators

defining the generator is nothing but creating
a function with yield  keyword.

if any function which is defined by using yield keyword
then that function will return generator object.

yield keyword will work same as return keyword,but
the difference is return keyword will return the value
and it will comes out from the function without
maintaing previous state.

yield keyword will return the value and it will
holds its state.

'''














