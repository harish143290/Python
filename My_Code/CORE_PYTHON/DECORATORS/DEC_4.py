
def division(x,y):
    z=x/y
    print("Result is : ",z)

def smart_division(func): #func is copy of division
    def wrapper(x,y):
        if y==0:
            print("<<< SORRY V R N D BY ZERO >>> ")
        else:
            func(x,y)

    return wrapper

#calling
division(10,3)
division(10,2)
#division(10,0)

print("========================")
division=smart_division(division) #inf is copy of wrapper
division(10,0)
division(10,3)




