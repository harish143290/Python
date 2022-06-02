
def greet(name):
    print("Hello "+name+" Have a nice day ...")

def dec_greet(func): #func is copy of greet
    def wrapper(name):
        if name=="roja":
            print("Hello "+name+" Have a good Day :)  ...")
        else:
            func(name) #calling greet(name)

    return wrapper
    
#calling
greet("sai")
greet("roja")
greet("shiva")
print("- "*30)

greet=dec_greet(greet)
greet("roja") 
greet("shiva")
greet("sai")




