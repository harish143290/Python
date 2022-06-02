import time

fsrc=None
ftrg=None

try:
    sfname=input("Enter SRC Filename : ") 
    fsrc=open(sfname,"r")

except FileNotFoundError:
    print("Sorry SRC File Is Not Existed ")

else:
    
    print("SRC Found ")
    tfname=input("Enter TRG Filename : ")
    try:
        ftrg=open(tfname,"x")
    except FileExistsError:
        print("Sorry TRG is already Existed ....")
    else:
        time.sleep(1)
        print("Data is coping....")
        data=fsrc.read()
        ftrg.write(data)
        time.sleep(1)
        print("Data is copied ....")    

finally:
    if fsrc!=None:
        fsrc.close()

    if ftrg!=None:
        ftrg.close()


        


        
