import time
class MyRange:
    def __init__(self,start,end):
        self.value=start
        self.end=end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value>self.end:
            raise StopIteration
        self.cur=self.value
        self.value=self.value+1
        return self.cur

'''calling'''
for i in MyRange(15,20):
    time.sleep(1)
    print(i)
