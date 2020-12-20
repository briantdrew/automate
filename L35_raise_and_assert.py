# you can raise your own exceptions in your own code

""" create box printing function

*********************************
*                               *
*                               *
*                               *
*                               *
*********************************
"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbol needs to be a string of length 1.')
    if (width < 2) or (height < 2):
        raise Exception(' width and height must be >=2')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    
    print(symbol * width)

boxPrint('*', 15, 5)
boxPrint('O', 5, 15)
boxPrint('o', 2, 2)

# but what happens with 2 symbols vs 1
boxPrint('*', 15, 5)
# it looks wonky, not what we intended but doesn't throw an exception
# so went back an inserted if len != 1 with raise Exception to address
# likewise a box of 1x1 is not really a box so added some code to 
#check for that

# can get traceback info back as a string value with traceback.format
# to get this block of code to work, fix 'exceptions' above
# make the 1 at least a 2 and the '**' a single '*'
import traceback
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('error_log.txt', 'a') # open in append mode to write
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback was written to error_log.txt')

# an assertion is a sanity check to make sure code isn't doing something obviously wrong

# assert keyword with condition. if condition evaluates to false, 
# the assertion error is thrown

assert False , "This is the assert error message" # just example, will always evaluate to false

