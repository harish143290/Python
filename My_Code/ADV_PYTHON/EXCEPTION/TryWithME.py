
''' Can i write more than one except for
    a single try ?
    Ans: Yes.
'''
import sys
try:
    x=int(sys.argv[1])
except IndexError:
    print("IE : Please Enter atleast one input ")
except ValueError:
    print("VE: Please Enter an int input only ")
else:
    print("Given Value is : ",x)
    
