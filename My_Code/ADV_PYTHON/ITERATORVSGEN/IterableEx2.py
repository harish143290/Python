import time

class courses:
    def __init__(self):
        self.lst=["Android","Java","Python","DM","Django"]
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        self.index+=1
        if self.index>=len(self.lst):
            raise StopIteration
        else:
            return self.lst[self.index]
        self.index=self.index+1

''' calling '''
for i in courses():
    time.sleep(1)
    print(i)

