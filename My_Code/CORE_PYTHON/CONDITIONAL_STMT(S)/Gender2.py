'''Accept a character from the user
    print Male if given char is m or M
    print Female if given char is f or F
    else third gender '''

gender=input("Enter any char : ")

#       0     1   2    3      slicing : [start : end : step ]
lst=['M','m','F','f']      

#if gender=='M' or gender=='m':
#if gender in lst[0:2]:
if gender in "mM":
    print("Male ")

#elif gender=='F' or gender=='f':
#elif gender in lst[2:]:
elif gender in "fF":
    print("Female")
    
else:
    print("Third Gender")




