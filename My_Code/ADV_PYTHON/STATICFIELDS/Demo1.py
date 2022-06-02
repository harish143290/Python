
class Sample:
    x=10 #static variable | Field

'''calling '''
#print("x val is : ",x) NameError
print("static x val is : ",Sample.x)
s=Sample()
print("static x val is : ",s.x) 
    
