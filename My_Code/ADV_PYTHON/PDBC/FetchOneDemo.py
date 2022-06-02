
import cx_Oracle
import time

conn=None
cur=None

try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl5")

except cx_Oracle.DatabaseError as e:
    print("Sorry unable to continue....")
    print("Reason : ",e)

else:
    print("Connection is Est ")
    cur=conn.cursor()

    print("Cursor object is created ")
    cur.execute("SELECT EMPNO,ENAME,JOB FROM EMP")
    t=cur.fetchone()
    print(t)

finally:
    if cur!=None:
        cur.close()

    if conn!=None:
        conn.close()

        
