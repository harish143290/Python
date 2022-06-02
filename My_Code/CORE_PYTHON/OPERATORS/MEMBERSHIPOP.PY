''' Membership operators can used only on iterables
        str | list | set | tuple | dict .....

    in --- returns True iff the specified object is existed
             in the iterable | collection

                    syn: object in iterable
                    
    not in -- returns True iff the specified object is not
    existed in the iterable | collection

                    Syn: object not in iterable
'''
lst=[10,20,30,40,50]
print("List : ",lst)
print("30 in lst ? : ",30 in lst)
print("90 in lst ? : ",90 in lst)

print("90 not in lst ? : ",90 not in lst)

s="WELCOME"   #str | iterable
print("s in welcome ? : ", 's' in s)
print("L in WELCOME ? : ",'L' in s)












