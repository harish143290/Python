'''cmd2.py
   prg to print all command line arguments...'''

import sys
import time

print("All Command Arguments ")

for i in sys.argv[1: ]:
    time.sleep(1)
    print(i)

