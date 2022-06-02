class Sample:
    def __init__(self):
        print("const is invoked ")

    def __del__(self):
        print("dest is invoked ")

'''calling'''
lst=[Sample(),Sample(),Sample()]
#del lst[1]
del lst
