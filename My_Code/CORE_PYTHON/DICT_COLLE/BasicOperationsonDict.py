#Basic Operations on Dict collection without using methods

#creating an empty dict
stu={} # or d1=dict()
print("Data is : ",stu)

#adding an item to dict collection
#D[k]=d
stu['sno']=101
stu['sname']='Ramesh'
print("After Adding items : ",stu)

#Updating item in dict collection
stu['sname']='Suresh'
print("After Updating : ",stu)

#Reading a value From dict collection
#D[k] -> v
name=stu['sname']
print("Sname is : ",name)
no=stu['sno']
print("Sno is : ",no)

#city=stu['scity'] KeyError

#Deleting an item from dict collection
#del D[k]
del stu['sno']
print("After Deleting an item : ",stu)













