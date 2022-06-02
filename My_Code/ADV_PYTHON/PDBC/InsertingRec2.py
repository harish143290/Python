import cx_Oracle

conn=None
cur=None

try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl5")

except cx_Oracle.DatabaseError as e:
    print("Sorry Unable to continue....")
    print("Reason ? \n : ",e)

else:
    print("Connection is Est ");
    cur=conn.cursor()    
    print("Cursor object is created ")

    que="INSERT INTO MYPYT7 VALUES(%d,'%s','%s')"

    while True:
        sno=int( input("Enter sno : ") )
        sname=input("Enter sname : ")
        scity=input("Enter scity : ")

        cur.execute(que %(sno,sname,scity))
        print(cur.rowcount," Rec is inserted ")

        opt=input("Do u want another Y | N : ")

        if opt in ['N','n']:
            break

    conn.commit()

finally:
    if cur!=None:
        cur.close()

    if conn!=None:
        conn.close()
    
