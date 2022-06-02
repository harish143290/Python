class Father:
    def house(self):
        print("house property from Father")

class Son(Father):
    def bike(self):
        self.house()
        print("bike from Son ")

'''calling'''
s=Son()
s.bike()
