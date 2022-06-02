'''cmd5.py'''

import sys
import re

m=re.fullmatch("[6-9][0-9]{9}",sys.argv[1])

if m!=None:
    print("Valid Mobile Number ")
else:
    print("Sorry Invalid Mobile number")
