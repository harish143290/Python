
class Mother:
    def color(self):
        print("Color from Mother ")

class Father:
    def height(self): 
        print("Height from Father ")

class Son(Father,Mother):
    def properties(self):
        self.color()
        self.height()
        print("Education from Son")

'''calling '''
s=Son()
s.properties()
