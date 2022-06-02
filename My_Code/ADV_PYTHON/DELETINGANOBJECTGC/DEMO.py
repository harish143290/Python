class Sample:
    def __init__(self):
        self.x=10
        self.y=20

    def getData(self):
        print("x val is : ",self.x)
        print("y val is : ",self.y)
        print("- "*20)

    def __del__(self):
        print("Object is Deleted....")
        print("R.D.A.Done....")
        print("- "*20)        

'''calling'''
s1=Sample()
s1.getData( )
s1=None
'''s1.getData( )  AttributeError '''

s2=Sample()
print("Data From s2 ")
s2.getData( )
s2=None



