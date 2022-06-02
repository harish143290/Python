'''
def biggest(x,y):
    if x>y:
        return x
    else:
        return y

big=biggest(110,20)
print("Biggest is : ",big)
'''

x=int(input("Enter First Number: "))
y=int(input("Enter Second Number : "))

biggest=lambda x,y : x if x>y else y
big=biggest(x,y)
print("Biggest is : ",big)




