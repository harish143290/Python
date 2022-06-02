
''' Back slash character or esc seq characters
       - These are used to produce the output
       in the user desired fashion

       \n   -> new line
       \t    -> tab space
       \a   -> bell sound
       \v   -> V tab

       \'   --> it will print ' symbol
       \"   --> it will print " symbol
       \\    ---> it will print \ sym

       \b  ---> backspace
       \r   ---   C.return | bring the cursor starting pos of the
                    same line        
      
'''

x=10
y=12.12
z="shashi"
print(x,y,z,sep='\'')
print(x,y,z,sep='\t')
print(x,y,z,sep='\n')
print(x,"\n",y,"\n",z)



















