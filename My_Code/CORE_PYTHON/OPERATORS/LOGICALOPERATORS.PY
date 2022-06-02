
''' Logical Operators are used to check  more than
one condition
     Eg: In Other Languages : and && | or || | not !  
     Eg: In Python :  and |  or | not   [keywords ]

logical and
              Example:
              Exp1        Exp2         Result
              True         False        False
              False        True         False
              False        False        False
              True         True          True
              
logical or
            Example:
            Exp1        Exp2         Result
              True         False        True
              False        True         True
              False        False        False
              True         True          True
              
logical not
       x,y=10,5
       print(x>y) # T
       print(not x>y) #F

       print(x<y) #F
       print(not x<y) #T
'''

x,y,z=10,20,30
print("x,y,z=10,20,30 ")
print("x>y and x>z ? : ",x>y and x>z) #F and F -> F
print("y>x and y>z ? : ",y>x and y>z) #T and F -> F
print("z>x and z>y ? : ",z>x and z>y) #T and T -> T
print("=================================")

x,y,z=10,20,30
print("x>y or x>z ? : ",x>y or x>z) #F or F -> F
print("y>x or y>z ? : ",y>x or y>z) #T or F -> F
print("z>x or z>y ? : ",z>x or z>y) #T or T -> T









