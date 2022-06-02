


f=open("data1.txt","w+")
print("Type is : ",type(f)) #<class '_io.TextIOWrapper'>

print("File name is : ",f.name)
print("File mode is : ",f.mode)
print("File closed ? : ",f.closed)

print("File Readable ? : ",f.readable())
print("File writeable ? : ",f.writable())

f.close()
print("File Closed ? : ",f.closed)
