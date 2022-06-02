import time

def sq(x):
    s=x*x
    return s

'''calling '''
time.sleep(1)
assert sq(2)==4," sq(2) should be 4 Only ..."
a=sq(2)
print("Result of sq(2) ? : ",a)

time.sleep(1)
assert sq(3)==9,"sq(3) should be 9 Only...."
a=sq(3)
print("Result of sq(3) ? : ",a)

time.sleep(1)
assert sq(4)==16, " sq(4) should be 16 Only..."
a=sq(4)
print("Result of sq(4) ? : ",a)
