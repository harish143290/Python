#    0   1    2   3    4   5
t=(10,20,30,10,50,60)
print("Tuple : ",t)

#T.index(item[,start,end])  | ValueError

pos=t.index(10)
print("Found @ : ",pos)

pos=t.index(10,3,6)
print("Found @ : ",pos)

#T.count(item[,start,end] ) -> int
no=t.count(10)
print("no.of.occ : ",no)

'''
Note: What is diff b|w list collection vs tuple collection

> List is mutable collection
> list is good if u r frequent operations
   are insertion and deletion

> tuple is immutable collection
> tuple is good if u r frequent operations are
   reading objects from the collection

> Reading values from the tuple collection is faster
than list collection reason is tuple is immutable thus
size fixed where list is mutable size is changing dynamicallt '''


























