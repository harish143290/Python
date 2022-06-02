#float typecasting using float( )
x=123
y=float(x)
print(type(x),"------>",type(y))
print(x,"----------> ",y)
print("- "*30)

x=(10+20j)
#y=float(x) TypeError: can't convert complex to float

x="123.1212"
y=float(x)
print(type(x),"------>",type(y))
print(x,"----------> ",y)
print("- "*30)

x=True   # True -> 1 -> 1.0   False --> 0 -> 0.0
y=float(x)
print(type(x),"------>",type(y))
print(x,"----------> ",y)
print("- "*30)







