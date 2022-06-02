import time

class A:
    pass

class B(A):
    pass

class C(B):
    pass

c=C()
for i in C.mro():
    time.sleep(1)
    print(i)

