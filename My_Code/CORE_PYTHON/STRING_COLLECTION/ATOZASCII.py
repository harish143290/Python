
import time

for i in range(65,91):
    time.sleep(.2)
    print(i,"---->",chr(i) )

print("=============")
s="abcedefgh"
for i in s:
    time.sleep(.2)
    print(i,"--->",ord(i) )
