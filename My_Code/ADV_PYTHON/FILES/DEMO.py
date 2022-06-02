
Working with Files
   Programs are classified into 2 types
   based on the storage of data in the memory
   
      1.Non Persistency Programs
          
      2.Persistency Programs
            a.By Using Files            
            b.By Using Databases

    File:
        open(str,str) -> File class object
          str rep name of the file
          str rep file mode

    FileModes :
        1."w" : write mode
           > If the specified file is already existed then
           it will open that file and overwrite old data with
           new data, but in this case old data is erased.

           > if the specified file is not existed then it will
           create a new file and allow for writing data into
           it.

        2."r": read mode
            > it is the default mode.
            > it will open the file and allow for reading data
            from it.
            > if the specified file is not existed then PVM will
            raise an Error : FileNotFoundError

        3."a": append mode
           > If the specified file is already existed then
           it will open that file and add new data to
           previous, but in this case old data is not erased.

           > if the specified file is not existed then it will
           create a new file and allow for writing data into
           it.

        4."x": exclusive
           > if the specified file is not existed then it will
           create new file and allow for writing data into it.

           > if the specified file is already existed then PVM
           will raise an Error: FileExistsError

       5.w+ : write + read
       6.a+  :  append + read

 Methods :
     name
     mode
     closed

     readable( )
     writeable( )
     close( )

For Writing Data Into the Files :
    write(data)
    writelines(iterable)

For Reading Data From the Files :
    read( ) -> str
    read(bytes) -> str
    readline( ) -> str
    readlines( ) -> list

    tell( )
    seek( )

Note: whenever u open the file in read mode then that
file u can use it as an iterable ie. we can use that one
in the for.

os.path.exists(path)
   - it will returns True iff the specified path is existed.
   
os.path.isfile(path)
   - it will returns True iff the specified path is a File.
   
os.path.isdir(path)
   - it will returns True iff the specified path is a directory.
   










    

          
        
 
