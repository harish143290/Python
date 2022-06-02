

'''
   (<expression> for variable in iterable if test)
                                 - generator collection | iterable
'''

t=(i for i in range(1,11) )
print("type is : ",type(t))
for i in t:
    print(i)
print("- "*20)

import time
for i in (i for i in range(1,21) if i%2==0 ):
    time.sleep(.2)
    print(i)
    

