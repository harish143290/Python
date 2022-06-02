'''MyDBInfo.py'''

import cx_Oracle
import time

def delete_rec(no):
    conn=None
    cur=None

    try:
        conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl5")

    except cx_Oracle.DatabaseError as e:
        print("Sorry unable to continue...")

    else:
        cur=conn.cursor()
        que="DELETE FROM EMP WHERE empno=%d"
        cur.execute(que %no)
        conn.commit()
        print(cur.rowcount," Rec are Deleted ....!!!")
    
    finally:
        if cur!=None:
            cur.close()

        if conn!=None:
            conn.close()
            



