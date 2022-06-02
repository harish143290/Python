
'''
  shashimodule.py | mainmodule
      Note: if the execution is started from the mainmodule
      then __name__ is __main__. if the execution is started
      from outside of mainmodule then __name__ is
      the modulename which is imported 
'''

def greet():
    print("- "*20)
    print("Hello Dear ")
    print("Have a nice day ")
    print("- "*20)

#calling
#print("Type of __name__ is : ",type('__name___'))
#print("Value of __name__ is : ",__name__)

if __name__=='__main__':
    greet()




    


