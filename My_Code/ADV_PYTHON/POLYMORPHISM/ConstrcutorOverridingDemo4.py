class A:
    def __init__(self):
        print("Def  of A ")

class B(A):
    def __init__(self):
        print("Def of B ")

class C(B):
    def __init__(self):
        super(B,self).__init__()
        super().__init__()        
        print("Def of C ")

'''calling'''
c=C()
