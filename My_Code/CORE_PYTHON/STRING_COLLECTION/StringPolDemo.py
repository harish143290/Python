# n="mom"
# reverse --> r="mom"
# we have to compare both actual string and reversed str
# if both are same then it is pol else not a pol

#App-1
n=input("Enter any String : ")
r=n[::-1]
if n==r:
    print("Polin")
else:
    print("Not")

#App-2:
n=input("Enter String :")
print("pol") if n==n[::-1] else print("Not")

