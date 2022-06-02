class Biggest:
    def setData(self,x,y):
        self.x=x
        self.y=y

    def findBiggest(self):
        if self.x>self.y:
            print("biggest is : ",self.x)
        else:
            print("biggest is : ",self.y)

'''calling'''
b=Biggest()
m=int(input("Enter First Number : "))
n=int(input("Enter Second Number :"))
b.setData(m,n)
b.findBiggest( )


