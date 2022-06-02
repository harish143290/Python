
'''
Can i handle any possiable exception by a single except ?
Ans: Yes, It is possiable by writing 'Exception' as an
argument to the except block or
except without Exception name '''

import sys

try:
    x=int(sys.argv[1])
    y=int(sys.argv[2])
    z=x/y

except:
    print("Sorry Dear ")
    print("We are unable to continue...")

else:
    print("Result is : ",z)




    
