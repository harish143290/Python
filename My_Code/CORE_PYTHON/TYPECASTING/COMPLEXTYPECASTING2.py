'''
complex(x) -> complex
    x rep real part , where y always remains 0j   

complex(x,y) -> complex
   x rep real part, where y rep imag part
   if x is string it won't take imag value.
   string with other combination are not supported 
'''
x=10
y=12.1212
z=complex(x,y)
print("Result is : ",z)

x=True
y=False
c=complex(x,y)
print("Result is :",c)

x="123"
y=12
#c=complex(x,y)
c=complex(y,x)    # "123"+12j Error
print("Result is : ",c)











