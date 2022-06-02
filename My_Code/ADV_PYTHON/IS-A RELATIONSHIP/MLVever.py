class GFather:
    def house(self):
        print("House From GFather ")

class Father(GFather):
    def car(self):
        print("Car From Father ")

class Son(Father):
    def properties(self):
        self.house()
        self.car()
        print("Bike From Son ")

'''calling'''
s=Son()
s.properties()


