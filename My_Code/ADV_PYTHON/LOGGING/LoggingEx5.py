
import logging


logging.basicConfig(filename="log7.txt", filemode="a", level=logging.DEBUG, format='%(asctime)s :%(levelname)s: %(message)s',datefmt='%d - %m - %Y %H:%M:%S %p')

logging.critical(' Critical information ')
logging.error(' Error message ')
logging.warning(' Warning message ')

logging.debug(' Debug Message ')
logging.info('Information')

print('Log File is Created ')
