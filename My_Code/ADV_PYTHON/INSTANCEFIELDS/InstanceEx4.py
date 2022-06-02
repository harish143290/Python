class Sample:
    def method1(self):
        self.x=10

'''calling '''
s1=Sample()
s1.method1()

s2=Sample()
s2.method1()

print("s1 x : ",s1.x)
print("s2 x : ",s2.x)

s1.x=99
print("s1 x : ",s1.x)
print("s2 x : ",s2.x)
