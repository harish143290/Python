'''
complex(x) -> complex
    x rep real part , where y always remains 0j   

complex(x,y) -> complex
   x rep real part, where y rep imag part
   if x is string it won't take imag value.
   string with other combination are not supported 
'''
x=10
y=complex(x)
print("Result is : ",y)

x=12.1212
y=complex(x)
print("Result is : ",y)

x="123"
y=complex(x)
print("Result is : ",y)

x=False
y=complex(x)
print("Result is : ",y)








