
sno=123
sname="Ramesh"
marks=99.876

'''
Output:
sno is : 123
sname is : Mr|Mrs.Ramesh
marks : False.  '''

print("sno is : "+str(sno))
print("sname is : Mr|Mrs."+sname)
print("marks : "+ str( not bool(marks) ))

