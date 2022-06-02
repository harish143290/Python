

import logging

1.We can create log file by using basicConfig( )
from logging module.

basicConfig( ) which req the following parameters.
   filename
         name of the log file
             Eg:  logging.basicConfig(filename="log1.txt")
             logging.basicConfig(filename="e:\\shashi\\log2.txt")

        filename is optional
           by chance if we fail to specify the filename
           then logging information will display on the screen
           which is not recommanded.
           
   filemode
           * file mode is optional
           
           * default file mode is "a"
              It will add new data to the log file without
              erasing Old data.

   Eg: logging.basicConfig
               (filename='log3.txt',filemode="a")
             
   level
        * Logging Levels are option
        * Default Logging level is WARNING
        
        Logging Level
        
           CRITICAL [50]
              Represent very serious problems where
              it required very high attention.
                  Application is really fine but it is fail to
                  execute @ client place bcoz missing some
                  Softwares.
                  
           ERROR [40]
              Represent serious problems
                 BCOZ missing the tables in the database.
             
           WARNING [30]
              Rep a warning message,some caution need to
              make the client to get some alert.
              
           INFO [40]
               Rep any normal message in the logger.
               
           DEBUG [50]
               debuggine related message.

              debug < info < warning < error < critical

                Note: default logging level is warning
                   i.e it will write either warning < error < critical

    logging.basicConfig(filename="log4.txt",
                        filemode="a",level=logging.WARNING)

    logging.basicConfig(filename="log4.txt",
                        filemode="a",level=logging.DEBUG)

    In order to write the different level information then
    we have to use the following methods.

        logging.critical('critical message')
        logging.error('error message')
        logging.warning('warning message')
        logging.info('info message')
        logging.debug('debug message')
        
        
    
   format='%(levelname)s'
                   %(message)s
                   %(asctime)s
   
   datefmt='%d | %m | %Y %H:%M:%S %p"
                                              %I 12 Hour format
                                              %H 24 hour format

   all the above  parameters are keyword only arguments.
       


   
