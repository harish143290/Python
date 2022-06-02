
''' globals( ) -> dict with all global
variables as key and their values
are value of that keys
../
d=globals( )  --->  d={'x':20}'''

x=20 #global variable
y=23

def myfun1():
    x=10 #local variable
    print("myfun1 ")
    print("local x val is : ",x)
    d=globals()
    print(d)
    print("global x val is : ",d['x'])
    print("global x val is : ",globals()['x'])
    print("global x val is : ",globals().get('x'))

#calling
myfun1()
