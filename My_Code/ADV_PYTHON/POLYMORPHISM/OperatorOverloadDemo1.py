

'''Operator overloading is the process
of providing some additional functionality to the
operator without effecting its pre-existed nature

Operator overloading is nothing overriding predefined
methods which are existed in object class.

For Every Operator there is a predefined method in the
object class.called magic methods

+      --->    __add__(self,other)
-       --->    __sub__(self,other)
*      --->     __mul__(self,other)
/      ---->    __div__(self,other)
//     ---->    __floordiv__(self,other)
%    --->     __mod__(self,other)

>      -->   __gt__(self,other)
>=    -->   __ge__(self,other)

<      --->     __lt__(self,other)
<=    --->     __le__(self,other)

==   -->      __eq__(self,other)
!=    -->      __ne__(self,other)
.
.
'''


class BookPython:
    def __init__(self):
        self.pages=100

    def __add__(self,other):
        return self.pages+other.pages

class BookJava:
    def __init__(self):
        self.pages=200

bp=BookPython()
bj=BookJava()
tnp=bp+bj          #''' bp.__add__(bj)   '''
print("Total Pages are : ",tnp)

x=10
y=20
s=x+y
print("Result is : ",s)

a="Sai"
b="baba"
c=a+b
print("Result is : ",c)






        
