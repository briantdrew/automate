import webbrowser, sys, pyperclip
#import sys to use commmand line programmatically and pyperclip to use clipboard

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

# check if command line arguments were passed
if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.']
    addresss = ' '.join(sys.argv[1:]) # get slice including 870 Valencia St.
else:
    address = pyperclip.paste()

webbrowser.open(https://www.google.com/maps/place/ + address)
