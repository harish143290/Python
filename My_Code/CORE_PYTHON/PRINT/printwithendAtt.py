
'''print( ) will print result on the screen and PVM throw
the cursor to the new line
        print( ) = printf( ) + \n
        default value for end attribute in print( ) is \n
'''
x=10
y=12.12
z="Shashi"

print(x)  #10
print(y)  #12.12
print(z)  #Shashi

print(x,end='\n')
print(y,end='\n')
print(z,end='\n')

print(x,end='')
print(y,end='')
print(z,end='\n')

print(x,y,z,sep='<<>>',end='')
print("James")

print(x,y,z,end='',sep='<<>>')
print("James")






