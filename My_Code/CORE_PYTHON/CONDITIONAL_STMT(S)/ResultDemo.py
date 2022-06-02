'''Accept 3 sub marks and print Pass if marks>34 in all
subject else print Fail '''

m1=int(input("Enter M1 : ")) #30
m2=int(input("Enter M2 : ")) #40
m3=int(input("Enter M3 : ")) #50

if m1>34 and m2>34 and m3>34:
    print("Pass")
else:
    print("Fail")

print("Pass") if m1>34 and m2>34 and m3>34 else print("Fail")
