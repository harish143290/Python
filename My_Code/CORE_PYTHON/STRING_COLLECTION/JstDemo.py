
#S.rjust(width,fillchar) -> str
import time

for i in range(1,10):
    time.sleep(.1)
    print(str(i).rjust(6,' '))
