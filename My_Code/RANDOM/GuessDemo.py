
import random
import time

lst=['pen','book','box','pencil','mouse','printer']
print("List : ",lst)

for i in range(1,11):    
    item=random.choice(lst)
    if item==input("Guess Item: "):
        print("U R Guess Corrent ")
        print("U WON that item For Free....")
        break
    else:
        print("Try again... ")

        
        
    
