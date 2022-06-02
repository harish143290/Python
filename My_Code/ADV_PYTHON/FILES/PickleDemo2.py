import mymodule
import pickle

f=open("myeinfo2.txt","wb")

while True:
    e=mymodule.Employee()
    e.setEmployee()
    pickle.dump(e,f)

    opt=input("Do u want another Rect Y | N ? : ")

    if opt in ['N','n']:
        break

f.close()
print("Recored are Saved ...!!!")


