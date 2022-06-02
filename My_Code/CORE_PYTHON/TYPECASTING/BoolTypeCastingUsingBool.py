# 1-true | 0-false
# in facts other than 0 is true

#bool type casting using bool( )
x=123
y=bool(x)
print(type(x),"------>",type(y))
print(x,"----------> ",y)
print("- "*30)

x=1.0
y=bool(x)
print(type(x),"------>",type(y))
print(x,"----------> ",y)
print("- "*30)

x=(0+1.23j)
y=bool(x)
print(type(x),"------>",type(y))
print(x,"----------> ",y)
print("- "*30)

x="123"
x="12.12"
x="(0+123j)"
x="0+0j"
x="False"
x="0"
x="shashi"
x=" "
x=""

x=0
x=0.0
x=(0+0j)
x=None
x=""
x=[]
x=()
x=set()
x={}
y=bool(x)
print(type(x),"------>",type(y))
print(x,"----------> ",y)
print("- "*30)












