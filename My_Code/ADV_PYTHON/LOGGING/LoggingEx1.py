
import logging


logging.basicConfig(filename="log1.txt",filemode="a")
logging.critical(' Critical information ')
logging.error(' Error message ')
logging.warning(' Warning message ')

logging.debug(' Debug Message ')
logging.info('Information')
