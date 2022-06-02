import time

lst=[10,20,30,40,50,60]
print("List : ",lst)

item=int(input("Enter an item : ")) #30

for i in lst:
    time.sleep(.2)
    if i==item:
        print("Found")
        break
        
