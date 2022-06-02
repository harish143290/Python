def smart_division(func): #func is copy of division
    def wrapper(x,y):
        if y==0:
            print("<<< SORRY V R N D BY ZERO >>> ")
        else:
            func(x,y)
    return wrapper

@smart_division #division=smart_division(division)
def division(x,y):
    z=x/y
    print("Result is : ",z)

#calling
division(10,3)
division(10,2)
division(10,0)

''' Note:
decorator are classified into 2 types
  1.Predefined decorator
      decorators which provided by PVM along with
      Python software called predefined decorators
               @abstractmethod
               @staticmethod
               @classmethod
               @property...
               
  2.Userdefined decorators
       - The decorators which are defined
       by us for our application req

            Eg: @smart_division
                   @special_greetings... '''



                   


       








  











