Oracle Basics :
 SQL>show user;
     - It will display the username

SQL>cl scr;
      - To clear the screen

Create
Syn: SQL>Create <table>  <tablename>
          (<column_name>    <datatype>(size),.......,
		    <column_n>            <datatype>(size) );

Eg:  SQL>Create table stupyt7
        (sno    number(3),
    	  sname  varchar(20),
		  scity      varchar(20) );
		  

SQL>select * from tab;
    - It will display all the object existed in the current user;


SQL>Desc[ribe]  <tablename>;
    - It will display description of the table.

ALTER :
   - We Can Add Column or Column(s)
   - We Can Change name of the column
   - We can drop a column(s)
   
  Syn:
  SQL>Alter <table>  <tablename>
  [ADD | DROP | MODIFY]
  (<column_name>   <datatype>(size),......)

SQL> ALTER TABLE STUPYT7
  2  ADD(FNAME VARCHAR(10),SPIN NUMBER(6));
Table altered.

Changing The Name of The Column:
SQL> ALTER TABLE STUPYT7
  2  RENAME COLUMN
  3  SNAME TO STU_NAME;

Table altered.

Delete a Column :
SQL> alter table stupyt7
  2  drop column spin;

Delete a group of column(s):
SQL> ALTER TABLE STUPYT7
  2  DROP
  3  (SCITY,FNAME);

Table altered.

Deleting Table:
Syn:
SQL>Drop <table>  <tablename>;
SQL>Drop table stupyt7;

INSERT :
SYN:
SQL>Insert <into>  <tablename>
(<column1>,<column2>,.......,<column n>)
values
(<value1>,<value2>,.....,<value n>);

SQL> INSERT INTO STUPYT7
  2  (SNO,SCITY)
  3  VALUES
  4  (101,'KMM');

Syn:
SQL>Insert <into>  <tablename>
Values
(<value1>,<value2>,....., <value n>);

SQL> INSERT INTO STUPYT7
  2  VALUES
  3  (102,'SHASHI','HYD');

Note: While inserting the data of type varchar and date
types then values must be enclosed in ' '

SELECT :
Syn:
SQL>SELECT [DISTINCT]  <columnname(s)>/[*]
          FROM  <tablename>
          [WHERE <condition>]
		  [ORDER By <Column> [DESC] ];


Note:  scott user is providing some predefined tables
in this account i.e emp | dept | bonus | salgrade ...

SQL> SHOW NUMWIDTH
numwidth 10
SQL> SET NUMWIDTH 5;
SQL>
SQL> SELECT * FROM EMP;

SQL> SELECT * FROM DEPT;

DEPTNO DNAME          LOC
------ -------------- --------
    10 ACCOUNTING     NEW YORK
    20 RESEARCH       DALLAS
    30 SALES          CHICAGO
    40 OPERATIONS     BOSTON


DISTINCT CLAUSE:
================
SQL>select JOB FROM EMP;
SQL>SELECT DISTINCT JOB FROM EMP;

ORDER BY CLAUSE:
==================
SQL>Select ename from emp;
SQL>Select ename from emp
                       Order by ename;
SQL>select ename from emp
                       order by ename desc;

SQL>select empno,ename,job,sal
from emp
order by ename;

 or

SQL>SELECT empno,ename,job,sal
from emp
order by 2;


WHERE CLAUSE:
==============
SQL> SELECT EMPNO,ENAME,JOB,SAL
  2  FROM EMP
  3  WHERE ENAME='SMITH';

EMPNO ENAME      JOB         SAL
----- ---------- --------- -----
 7369 SMITH      CLERK       800

SQL> SELECT *
  2  FROM EMP
  3  WHERE ENAME='SMITH';

EMPNO ENAME      JOB         MGR HIREDATE
----- ---------- --------- ----- ---------
 7369 SMITH      CLERK      7902 17-DEC-80

 SQL> select EMPNO,ENAME,JOB,SAL,HIREDATE
  2  FROM EMP
  3  WHERE JOB='MANAGER';

EMPNO ENAME      JOB         SAL HIREDATE
----- ---------- --------- ----- ---------
 7566 JONES      MANAGER    4975 02-APR-81
 7698 BLAKE      MANAGER    4850 01-MAY-81
 7782 CLARK      MANAGER    4450 09-JUN-81

 SQL> SELECT * FROM EMP
  2  WHERE HIREDATE='02-APR-81';

EMPNO ENAME      JOB         MGR HIREDATE
----- ---------- --------- ----- ---------
 7566 JONES      MANAGER    7839 02-APR-81


 SQL> SELECT *
  2  FROM EMP
  3  WHERE JOB='SALESMAN'
  4  ORDER BY ENAME;

EMPNO ENAME      JOB         MGR HIREDATE
----- ---------- --------- ----- ---------
 7499 ALLEN      SALESMAN   7698 20-FEB-81
 7654 MARTIN     SALESMAN   7698 28-SEP-81
 7844 TURNER     SALESMAN   7698 08-SEP-81
 7521 WARD       SALESMAN   7698 22-FEB-81


SQL> SELECT *
  2  FROM EMP
  3  WHERE SAL<=4500 AND DEPTNO=20;

EMPNO ENAME      JOB         MGR HIREDATE
----- ---------- --------- ----- ---------
 7369 SMITH      CLERK      7902 17-DEC-80
 7876 ADAMS      CLERK      7788 23-MAY-87


I-Insert
C-Create
U-Update
R-Read [ SELECT ]
D-Delete


UPDATE:
==========
SQL>update <table>
SET <column>=<value>,<column>=<value>....
[WHERE <condition>];

SQL>UPDATE EMP SET COMM=9999;

SQL> UPDATE EMP
  2  SET COMM=9999
  3  WHERE COMM IS NULL;


 SQL> UPDATE EMP
  2  SET SAL=SAL+(SAL*10)/100,
  3      COMM=COMM+(COMM*5)/100
  4  WHERE JOB='SALESMAN';

rollback :
   It is used to cancel last Transaction
   [ Rollback will Work on insert | update | delete operation ]

 SQL>Rollback;


DELETE:
SQL>DELETE <from> <tablename>
[WHERE <condition>];

  commit
  sql>COMMIT;
     Once transcation is commited rollback doesn't works
	 on it.























