
''' can i handle more than one exception
    using single except ?
    Ans: Yes, It is possible by writing all possible
    exceptions in the except block in the form of tuple
'''

import sys

try:
    x=int(sys.argv[1])

except (ValueError,IndexError):
    print("VE or IE : Please Enter an int input only...")

else:
    print("Given Input is : ",x)

    

