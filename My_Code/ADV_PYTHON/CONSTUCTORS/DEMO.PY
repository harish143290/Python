'''
Constructors:
    IQ: Can i create an object for a class without
    constructor ?
    Ans : No

    IQ: can i create an object for an empty class ?
    Ans : yes.

    Note: if the class is not defined with any constructor
    then PVM will create one constructor in that class
    classed 'default' constructor

    with the help of that constructor we can create
    an object for that class.

    1.Constructor name must be __init__(self)
    2.Constructor can return Only None not other types
    3.Constructor can be parameterized    
'''

class Sample:
    pass

s=Sample()
print("Content of Sample  class ")
print( dir(s) )
print("- "*30)

class Shashi:
    pass

print(dir(Shashi))

    
