
class Sample:
    def __init__(self):
        print("Def constructor of Sample")
        self.x=10
        self.y=20

    def getData(self):
        print("x val is : ",self.x)
        print("y val is : ",self.y)

'''calling'''
s=Sample( )
s.getData( )

s2=Sample()
s2.getData()

s3=Sample()
s3.getData( )
