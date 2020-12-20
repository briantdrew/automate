#python has a logging function.and this is the setup code, first import logging
import logging
#then this line which formats the entries in the log file
#log levels - debug(lowest), info, warning, error, critical(hightest)
# first run I didn't use a log file, just logged to screen, to log to a file
# add the filename = xxxxxx as shown...
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# to turn logging off, in this example from the CRITICAL log level and lower

#logging.disable(logging.CRITICAL)

#now we make a buggy factorial program with logging and see what happens

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial (%s)')
    total = 1
    #the result of zero is because the range was started with a zero and anything x 0 = 0
    # initial range was/is for i in range(n+1) 
    # remember range starts at zero when given 1 argument, so need to use (1, n+1)
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')

