
'''accept a char from the user print Male if given char is
m or M else print Female '''

gender=input("Enter any char ") #M

if gender=='m' or gender=='M':
    print("Male ")
else:
    print("Female")

print("Male ") if gender=='m' or gender=='M' else print("Female")
