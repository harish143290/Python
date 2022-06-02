
def greet():
    s="Hello  "
    return s

def specialGreetings(func):  #func is copy of greet
    n=func() #calling greet()
    m=n+" My Dear Lovely..!!!"
    return m

#calling
a=greet()
print("Result of greet ? : ",a)

b=specialGreetings( greet )
print("Result of SpecialGreetings : ",b)
