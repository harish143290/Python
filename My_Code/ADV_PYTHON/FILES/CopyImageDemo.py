
'''copy image from one to another location '''

fsrc=open("e:\\adv_super\\html\\f.jpg","rb")
b=fsrc.read()
print("Type is : ",type(b))


ftrg=open("myflower.jpg","wb")
ftrg.write(b)
print("Image is copied ")

fsrc.close()
ftrg.close()
