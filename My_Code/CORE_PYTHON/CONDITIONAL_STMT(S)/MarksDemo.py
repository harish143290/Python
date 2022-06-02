
''' accept 3 sub marks from the user calculate
    total , avg , findout result and grade
        if marks>34 in all sub then result is "Pass" else "Fail"
        if Result is pass
           then check the avg. if avg>=70 print Grade A
                                                 if avg>=60 print Grade B
                                                 if avg>=50 print Grade C
                                                 else Grade D '''
m1=int(input("Enter m1 : "))
m2=int(input("Enter m2 : "))
m3=int(input("Enter m3 : "))

tot=m1+m2+m3
avg=tot/3

if m1>34 and m2>34 and m3>34:
    if avg>=70:
        print("Grade A")
    elif avg>=60:
        print("Grade B")
    elif avg>=50:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("Fail")





