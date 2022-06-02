
1.Inorder to interact with Oracle Database
we have collection of classes | methods |
and functions from cx_Oracle module.

2.cx_Oracle Modules is not available along with Python
installation.Thus we have to install sep. by using PIP Tool

3.Python Installing Packages [PIP]
       this command must be executed from command prompt
          Syn: >>>pip install batteryname
                   >>>pip install cx_Oracle

STEPS FOR PDBC :
    1. import cx_Oracle and if required other modules.

    2.Est connection with Oracle Database
           by using the following function from cx_Oracle i.e
           connect(str,str,str) --> connection object.

           str --> username in the database Eg: scott
           str --> password of the user in db Eg: tiger
           str --> DB information
                        IPADDRESS : port number / serviceid
                        localhost:1521/orcl5

           note : For Every Database there is unique port number
           and service id .default port number for oracle Database
           is 1521 and service id of Oracle DB : orcl
               in my system SID : orcl5

           If any thing went wrong the PVM will raise an Exception
           cx_Oracle.DatabaseError 
                        
           Note: If u want know the service id of the Oracle
           Database then we have to use
                SQL>select * from global_name;


Example:
import cx_Oracle

conn=cx_Oracle.connect
     ("scott","tiger","localhost:1521/orcl5")

if conn!=None:
    print("Connection is Est ")
else:
    print("Connection is Fail ")


      3.Create cursor object for sending queries to DB
          To create an object of cursor class then we have to use
          the following method from connection class.i.e
                      cursor( ) -> cursor object
                      Eg:  cur=conn.cursor()

      4.Use the cursor object for sending queries to
      execute @ Database. by using the following method
      from cursor class.
                     execute(str)
                        ''' str rep any sql query | create | insert |
              update | delete | select .... '''
            Eg: cur.execute("create table ssinfo(sno number(2)")

       Note: After performing Insert | update | delete
       operations then we must call commit() from connection
       class otherwise those changes are not effected @ DB.
                           Eg: conn.commit()

        Note: If u want cancel Last transaction then we
        have to call rollback() from connection class.
                              Eg: conn.rollback()


        *** 
        Note : If we execute "select" statement then result
        of the select statement will be stored in the same
        cursor object only.

        Inorder to get that record then we have to use
            the following methods from cursor class.
                        fetchone( ) -> tuple
                        fetchmany() -> list of tuples
                        fetchall( ) -> list of tuples

        5.Process the Database result @ PDBC Programs
        6.Close the cursor and connection objects
                Eg:  cur.close( )
                        conn.close( )


                        

        

                           
             
           










    

