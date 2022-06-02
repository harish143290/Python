d1={"sno":101,"sname":"ramesh","scity":"hyd"}
print("D1 : ",d1)

#D.popitem() -> tuple | LIFO | KeyError
item=d1.popitem()
print("Deleted Item is : ",item)
print("D1 :",d1)

#D.pop(k[,d])->d | KeyError if specified k is not existed
#pop( ) -> d if specified k is not existed and when d is given
d=d1.pop("sno")
print("value of sno : ",d)
print("After POP : ",d1)

#D.clear( )
d1.clear()
print("D1 : ",d1)



