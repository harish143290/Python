
'''
  Generate CAPTCHA
     first 2 position digits
     3rd and 4th position should Uppercase letter
     5th position is digit
     6th position is lower case
'''

import random
import time

for i in range(1,11):
    time.sleep(1)
    print( random.randint(11,99),
               chr(random.randint(65,90)),
               chr(random.randint(65,90)),
               random.randint(1,9),
               chr( random.randint(97,122)),sep='')



