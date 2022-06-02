#Checking the substring using member ship op
# in and not in
'''
print('s' in 'welcome') #False
print('w' in 'welcome') #True   '''

main=input("Enter Main String : ")
sub=input("Enter Sub String : ")

if sub in main:
    print(sub, " is existed in ",main)
else:
    print(sub, " is not existed in ", main)

