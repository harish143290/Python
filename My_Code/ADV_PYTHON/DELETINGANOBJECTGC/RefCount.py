import sys

class Sample:
    def __init__(self):
        print("const is invoked ")

    def __del__(self):
        print("dest is invoked ")

'''calling'''
s1=Sample()
s2=s1
print("Ref_Count is : ",sys.getrefcount(s1))
s2=None
print("Ref_Count is : ",sys.getrefcount(s1))
s1=None

