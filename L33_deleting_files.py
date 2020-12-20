# since I've run these they are gone and so script bombs
# because they no longer exist but the tools can't handle that

# the deleting functions do not send to recycle bin, they are gone gone
# can do a dry run as seen later
import os
# ths method permanenly deletes a single file
os.unlink('/Users/btdrew/bastion.pem')
# to delete a EMPTY folder use os.rmdir - remove directory
os.rmdir('WorkDocs/test') # not empty so won't work
#to delete a folder and its contents, import shutil
import shutil
#and use remove tree 
shutil.rmtree('WorkDocs/test') #relative path in pwd /Users/btdrew
# dry run example comments out the executable piece, os.unlink
#and instead put a print statement to see what would happen

import os
for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)
 ## the above are unrecoverable but can use send2trash which
 import send2trash
 send2trash.send2trash('/Users/btdrew/mydata.db')
 