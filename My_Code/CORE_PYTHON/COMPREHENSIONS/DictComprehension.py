'''
   {<expression> for variable in iterable if test}
                                 - dict collection | iterable
                                 - expression should be in the form k:v
'''

d={i:i for i in range(1,5) }
print("Type is : ",type(d))
print("dict : ",d)
print("- "*30)

d2={i: i*i for i in range(1,5)}
print("dict : ",d2)
print("- "*30)

d3={i:i**i for i in range(1,5) if i%2==0 }
print("dict : ",d3)
print("- "*30)

import math
d4={ i:math.factorial(i) for i in range(1,6) }
print("dict : ",d4)









