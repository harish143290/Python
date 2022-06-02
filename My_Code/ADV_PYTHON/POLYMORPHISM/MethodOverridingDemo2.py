class Shashi(object):
    def __init__(self):
        self.name="Shashi"
        self.job='Digital IT Coach'

    def __str__(self):
        return self.name+" woking as "+self.job

''' calling '''
t=(10,20,30,40)
lst=list(t)
print("List : ",lst)

s=Shashi()
print("Shashi : ",s)

t=tuple()
print("tuple : ",t)

'''Note: While printing reference variable internally
PVM calls __str__(self) dunder method from object
class it return str type  '''





        
