def dec_greet(func): #func is copy of greet
    def wrapper(name):
        if name=="roja":
            print("Hello "+name+" Have a good Day :)  ...")
        else:
            func(name) #calling greet(name)

    return wrapper

@dec_greet  #greet=dec_greet(greet)
def greet(name):
    print("Hello "+name+" Have a nice day ...")
    
#calling
greet("sai")
greet("roja")
greet("shiva")
print("- "*30)




