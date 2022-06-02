import cx_Oracle

conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl5")

if conn!=None:
    print("Connection is Est ")

    cur=conn.cursor()
    print("Cursor Object is Created ")

    que="CREATE TABLE MYPYT7(SNO NUMBER(3),SNAME VARCHAR(20),SCITY VARCHAR(20))"
    cur.execute(que)
    print("Table is Created ")

    cur.close()
    conn.close()
    
else:
    print("Connection is Fail")
