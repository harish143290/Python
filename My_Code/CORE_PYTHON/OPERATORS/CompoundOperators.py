''' shortcut operators | compound operators
        combination of both arithmetic and assignment
           += |  -= | *= | /= | **= | %= | //=

           x+=10   -->   x=x+10
           y-=x      --->  y=y-x

           x++ Error
           x+=1 or x=x+1
'''
x,y=10,5
x+=y #x=x+y  ---> x=10+5
print("x val is : ",x)

x-=y #x=x-y ---> x=x-y
print("x val is : ",x)

x/=y  #x=x/y
print("x val is : ",x)

x=10
x//=y
print("x val is : ",x)




