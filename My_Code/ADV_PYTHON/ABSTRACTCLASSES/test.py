class C:
    count = 0 
    def __init__(self):
        self.I = C.count
        C.count = C.count + 1
    def getcount(self):
        return self.I