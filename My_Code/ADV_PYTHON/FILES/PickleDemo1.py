
import pickle
import mymodule

e=mymodule.Employee()
e.setEmployee()

f=open("myeinfo.txt","wb")
pickle.dump(e,f)

f.close()
print("Object is Created ")
