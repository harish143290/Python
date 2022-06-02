

'''
   {<expression> for variable in iterable if test}
                                 - set collection | iterable
'''

s={i for i in range(1,11)}
print("Type is : ",type(s))
print("Set : ",s)

s2={i for i in range(1,51) if i%3==0 or i%7==0 }
print("Set : ",s2)

