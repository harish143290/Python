
import cx_Oracle,time

conn=cur=None

try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl5")    

except cx_Oracle.DatabaseError as e:
    print("Sorry Unable to continue....")
    print("Reason  ? : ",e)
    
else:
    print("Connection is Est ")
    cur=conn.cursor()
    print("Cursor object is Created ")

    cur.execute("SELECT EMPNO,ENAME,JOB FROM EMP")
    lstoft=cur.fetchmany(5)

    for t in lstoft:
        time.sleep(1)
        print(t)   

finally:
    if cur!=None:
        cur.close()

    if conn!=None:
        conn.close()
        
