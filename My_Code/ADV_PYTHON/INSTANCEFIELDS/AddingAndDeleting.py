class Sample:
    pass

'''calling '''
s1=Sample()

''' print("s1 x : ",s1.x) AttributeError '''

'''Adding an instance field'''
s1.x=10
print("s1 x : ",s1.x)

''' updating an instance field '''
s1.x=99
print("s1 x : ",s1.x)

'''deleting an instance field '''
del s1.x
''' print("s1 x : ",s1.x) AttributeError '''
