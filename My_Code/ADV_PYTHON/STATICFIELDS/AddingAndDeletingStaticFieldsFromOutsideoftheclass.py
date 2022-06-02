class Student:
    pass

'''calling'''
#print("Sname is : ",Student.sname) AttributeError

Student.sname="Pooja"
print("Sname is : ",Student.sname)
s1=Student()
print("Sname is : ",s1.sname)

del Student.sname
#print("Sname is : ",Student.sname)

s1.course="Python"
#print("course is : ",Student.course) AE
print("course is : ",s1.course)

'''
   How to Add instance fields to the object from outside
   of class.
            Syn: <objectreference>.<filename>=<value>
                               s1.course="Python"

   How to Add static variable to the class from
   outside of that class.
             Syn: <classname>.<vname>=<value>
                              Student.city="Hyd"

    We can access static variable from outside of the
    class if it is existed in the class.either by using
    classname or object reference
                        print(Student.city)
                        print(s1.city)
                
    Instance fields must be referred by an object reference
    whenever u want access it from outside of the class.
                        print(s1.course)   
                     
'''





