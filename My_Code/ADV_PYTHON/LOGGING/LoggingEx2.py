
import logging


logging.basicConfig
(filename="log2.txt",filemode="a",level=logging.DEBUG)

logging.critical(' Critical information ')
logging.error(' Error message ')
logging.warning(' Warning message ')

logging.debug(' Debug Message ')
logging.info('Information')

print('Log File is Created ')
