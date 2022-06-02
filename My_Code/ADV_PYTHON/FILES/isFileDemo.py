
import os.path

if os.path.exists("e:\\adv_super\\app1.java"):
    print("Path Is Existed ")

    if os.path.isdir("e:\\adv_super\\app1.java"):
        print("Path is directory")
    else:
        print("Path is a file")
        
else:
    print("Sorry Path Is Not existed ")
