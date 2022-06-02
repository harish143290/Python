import cx_Oracle

conn=None
cur=None

try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl5")

except cx_Oracle.DatabaseError as e:
    print("Sorry Unable continue...")
    print("Reason  : \n ",e)

else:
    print("Connection is Est ")
    cur=conn.cursor()
    print("Cursor object is Created ")

    que="UPDATE EMP SET SAL=SAL+%d where job='%s'"
    inc_sal=int(input("Enter Increment Salary : "))
    job_title=input("Enter Job Title : ")

    cur.execute(que %(inc_sal,job_title))
    print(cur.rowcount," Rec are updated ....!")
    conn.commit()   

finally:
    if cur!=None:
        cur.close()

    if conn!=None:
        conn.close()

        
