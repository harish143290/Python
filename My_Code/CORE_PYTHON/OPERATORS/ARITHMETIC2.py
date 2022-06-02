''' What is diff / [division] vs // [floor division]
       division / operator always returns the result
       in the form float type.
              int / int -> float    
              float / int -> float
              int / float -> float
              float / float -> float

       floor division // returns the values based on
       the operand types and it will return only floor
       value but not scale value.
             int // int -> int                 10//3 -> 3
             float // float -> float      10.0//3.0 --> 3.0
             int // float --> float
             float // int --> float
'''
print("10/3   ? : ",10/3)
print("10/3.0   ? : ",10/3.0)
print("10.0/3   ? : ",10.0/3)
print("10.0/3.0   ? : ",10.0/3.0)
print("==========================")

print("10//3   ? : ",10//3)
print("10//3.0   ? : ",10//3.0)
print("10.0//3   ? : ",10.0//3)
print("10.0//3.0   ? : ",10.0//3.0)















