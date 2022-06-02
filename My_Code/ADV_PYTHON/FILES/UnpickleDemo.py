
import pickle

f=open("myeinfo.txt","rb")
e=pickle.load(f)
e.getEmployee()
f.close()
