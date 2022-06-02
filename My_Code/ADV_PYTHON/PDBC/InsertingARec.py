
import cx_Oracle

conn=None
cur=None

try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl5")

except cx_Oracle.DatabaseError as e:
    print("Sorry unable to continue ....")
    print("Reason ? : \n ",e)

else:
    print("Connection is Est ")
    cur=conn.cursor()
    print("Cursor Object is Created ....")

    que="INSERT INTO MYPYT7 VALUES(101,'MANI','HYD')"
    cur.execute(que)
    conn.commit()

    print(cur.rowcount," Rec are inserted ....! ")

finally:
    if cur!=None:
        cur.close()
        
    if conn!=None:
        conn.close()




