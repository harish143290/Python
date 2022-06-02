
import logging

logging.basicConfig(filename="logimp1.txt",level=logging.DEBUG,filemode="a",format='%(asctime)s:%(levelname)s: %(message)s',datefmt='%d / %m / %Y %H:%M:%S %p')
logging.info("============================")
logging.info('Request From Client .....')

try:
    x=int( input("Enter a number : ") )
    y=int( input("Enter a number : ") )
    z=x/y

except ValueError as ve:
    print("Sorry unable to continue....")
    logging.exception(ve)

except ZeroDivisionError as de:
    print("Sorry Unable to continue....")
    logging.exception(de)
    
else:
    print("Result is : ",z)
    print("Request is Executed Success....")
    




    
    

