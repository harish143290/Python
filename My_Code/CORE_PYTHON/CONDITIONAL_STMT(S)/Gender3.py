''' Nested if...
     accept gender and age from the user and findout
     status of the condidate

      if gender is M | m
          then check age if age>=21 print Major else minor

      if gender is F | f
         then check age if age>=18 print Major else minor

      else print Thrid Gender

'''


gender=input("enter gender : ")
age=int(input("enter age : "))
lst=['m','M','F','f']
#        0    1    2   3

if gender in lst[0:2:]:
    if age>=21:
        print("Major")
    else:
        print("Minor")

elif gender in lst[2:]:
    if age>=18:
        print("Major")
    else:
        print("Minor")
        
else:
    print("Third Gender")
    
















