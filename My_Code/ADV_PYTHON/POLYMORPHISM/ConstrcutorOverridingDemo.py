
class Super:
    def __init__(self):
        print("def const of Super ")

class Sub(Super):
    def __init__(self):
        super().__init__()
        print("def const of Sub ")

'''calling'''
s=Sub()
