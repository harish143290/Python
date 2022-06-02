'''
  [<expression> for variable in iterable
                              for variable in iterable
                              if test ]                                 
'''

lst=[ (i,j) for i in ["1","2"] for j in ["A","B"]  ]
print("Result is : ",lst)

import time
lst3=(i*j for i in [1,2,3] for j in ['A','B'])
for i in lst3:
    time.sleep(1)
    print(i)
