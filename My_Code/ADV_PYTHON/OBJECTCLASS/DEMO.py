
'''
 object :
    Object is the super class for every class in Python.

    1.if any class is inherited by other class then that
    class is indirect sub class of object.

    2. if any class is not inherited by other class then that
    class is direct sub class of object. '''

class A:
    pass

class B(A):
    pass

class C(object):
    pass

print("A is subclass of object ? : ",issubclass(A,object))
print("B is subclass of object ? : ",issubclass(B,A))
print("B is subclass of object ? : ",issubclass(B,object))
print("C is subclass of object ? : ",issubclass(C,object))

class D:
    pass

''' How many methods are their in the class D ?
    Ans : All the methods of object class.
    object is the super class for every class in Python.
'''






    

    
