 threading module
    Ways to define Threads
       1.Creating Thread by using an already existed fun.               
       2.Creating Thread by creating non sub class of thread
       3.Creating Thread by creating sub class of thread.
           In This app.
           
             1.Create Any class as the sub class of Thread

             2.Whatever the logic u want execute as thread
                 then that logic must be defined inside of
                 run( ) of thread class.

            3.we should not call run( ) of thread class rather
            we have to call start( ) of thread class for execution
            of Thread.

V.I.Note:
    > Default Thread In Python is Main Thread
    > Main Thread is auto executed Thread By PVM

Note:
    Whenever we define any thread by default
    Every thread is having its own name default name
    default name for thread are starts like

       thread-1, thread-2 ....

    Based On the application req we can get name of
    thread and we can change the name of the Thread
    by using

    setName(str);  or name=str
    getName() -> str or name attribute
    
 Note: To get the Object Of Current Working Thread
 then we have to use
     threading.current_thread( ) -> Thread

     active_count()
     is_alive()
     ident
     enumerate()






     







     



















                 

       
