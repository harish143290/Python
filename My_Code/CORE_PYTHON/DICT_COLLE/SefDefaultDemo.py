
#D.update({k:d})
#D.copy( ) -> shallow copy of dict

#D.keys( ) ->    <class 'dict_keys'>
#D.values( ) -> <class 'dict_values'>
#D.items( ) ->   <class 'dict_items'>

#D.pop(k[,d])
#D.popitem( ) -> tuple
#D.clear( )

stu={}
stu.update({"sno":101})
print("stu : ",stu)
stu.update({"sno":222})
print("stu : ",stu)
print("--------------------------------------")

#D.setdefault(k,d=None)
stu.setdefault("sname","Ramesh")
print("stu : ",stu)
stu.setdefault("sname","suresh")
print("stu : ",stu)
stu.setdefault("scity")
print("stu : ",stu)













