
Data types :
      * Rep type of data to be allowed in the memory.
      
      * In statically typed languages, we must specify
      the data type by time of declaring the variables.
         Eg: in C,C++ and Java
                     int eno=101;

      * In Dynamically typed languages, the type of
      variable will dicided by by PVM Based on the values
      we assigned to it.
                   Eg:  JavaScript | Python
                                 eno=101

        * In Python Data types are classified into 3 types
                   > value types
                          Number types
                               int
                               float
                               complex
                               Number Systems:
                                   decimal | binary | octal | hexa 
                          bool
                          None
                   > collection types
                            sequences | iterables
                            list | set | tuple | dict | str ...
                            
                   > binary types
                              bytes
                              bytearray

    * In Python Every Data type is class
              int --->  <class 'int'>
              str --->  <class 'str'>
              list --->  <class 'list'>

    * In Python Memory every thing will be stored in the
    form an object [ Memory block ]

        Objects are 2 types
             1.mutable objects
             
             2.immutable objects
                   Which doesn't allow to make the
                   changes in the same object,
                   rather it will create a new object
                   with modified content.

                      Eg: Number types | bool | str | tuple

        * Objects are dynamic in size thus there is no
           ranges and size for data types.

     int type:
          > Predefined class For int type is <class 'int'>
          > if any variable is assigned with a number
          without decimal then they are considered by
          PVM as int
          Eg:  sno=101
                  htno=1234567          

     float type:
           > predefined class for float is <class 'float'>
           > if any variable is assigned with a number
           with decimal value then they treated as
           float type.

           Eg:  x=3.14
                   y=1.2e2
                   z=1.2E3

    Complex type:
        * Predefined class For complex type is <class 'complex'>
        * Used to for mathametic and Eng Related Prgs.
        * Complex numbers rep in maths like a+bi
                            Eg: a+bi
                            a rep real
                            b is image
                            i under sqrt of -1

        * In Python complex numbers are rep by using
                           (a+bj) Here j is undersqrt of -1

        * real and image values can be either of
        type int or float but internally they will
        be stored as float.

        a=10+20j
        type(a)
        print(a.real) # 10.0
        print(a.imag) #20.0
        print(type(a.real) ) #<class 'float'>
        print(type(a.imag)) #<class 'imag'>

        NoneType
        x=10
        x=None

        del vs None
           del variable
           del variable,variable,.....

        bool  --> predefined class for bool type <class 'bool'>
          C-Language :    0-False | 1-True
          Java : false | true
          Python : False | True

          x=True | False

          
          

          
          
          






        










        









                            







                   






          
          

        
           

          
        
            

                   










    

    



                

                              







                   
      
