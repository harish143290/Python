f=open("data4.txt")
data=f.read(5)
print(data)

pos=f.tell()
print("File is Pointed @ : ",pos)

data=f.read(10)
print(data)
pos=f.tell()
print("File is pointed @ : ",pos)

f.seek(0)
pos=f.tell()
print("File is pointed @ : ",pos)

data=f.read()
print(data)
