
class A:
    pass

class B:
    pass

class C(A,B):
    pass

'''calling '''
c=C()
lst=C.mro()
print(lst)
