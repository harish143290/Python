
import cx_Oracle
import time
import csv

conn=None
cur=None
f=None

try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl5")
    
except cx_Oracle.DatabaseError as e:
    print("Sorry unable to continue....")
    print("Reason : \n ",e)

else:
    cur=conn.cursor()
    que="SELECT * from EMP WHERE JOB='%s'"
    jobtitle=input("Enter Job Title :").upper()
    cur.execute(que %jobtitle)   

    f=open(jobtitle+".csv","w",newline='')
    csvwo=csv.writer(f)
    
    for t in cur:
        time.sleep(1)
        csvwo.writerow([t[0],t[1],t[2],t[3]])

    time.sleep(1)
    print("Data is Copied ")

finally:
    if f!=None:
        f.close()
        
    if cur!=None:
        cur.close()
        
    if conn!=None:
        conn.close()
