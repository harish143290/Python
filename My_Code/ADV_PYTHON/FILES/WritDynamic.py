


f=open("data3.txt","w")
data=input("Enter U r data press * for Exit ") 

while data!='*':
    f.write(data+"\n")
    data=input() 

f.close()
print("Data is Saved ")
