class Calc:
    @staticmethod
    def add(x,y):
        s=x+y
        print("Add is : ",s)

    @staticmethod
    def  sub(x,y):
        s=x-y
        print("Sub is :",s)

'''calling'''
c=Calc()
c.add(10,20)
c.sub(10,2)
        
