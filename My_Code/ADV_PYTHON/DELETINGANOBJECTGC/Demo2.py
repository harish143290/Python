
class Sample:
    def __init__(self):
        print("const is invoked ")

    def __del__(self):
        print("dest is invoked ")

'''calling'''
s1=Sample()
s2=s1
s3=s2
s3=None
s2=None
s1=None
