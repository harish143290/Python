#int typecasting using int( )
print("float --> int ")
x=12.1212
y=int(x)
print(type(x),"------>",type(y))
print(x,"----------> ",y)
print("- "*30)

print("complex --> int ")
x=(10+20j)
#y=int(x)TypeError: can't convert complex to int
print("- "*30)

print(" str ---> int ")
x="120"
y=int(x)
print(type(x),"------>",type(y))
print(x,"----------> ",y)
print("- "*30)

print(" bool --> int ")
x=True
y=int(x)
print(type(x),"------>",type(y))
print(x,"----------> ",y)
print("- "*30)
