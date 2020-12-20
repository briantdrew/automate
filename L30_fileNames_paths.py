import os
print (os.path.join('folder1', 'folder2', 'folder3', 'file.png'))
#to get the current working directory cwd...
print(os.getcwd())
#to change current directory
os.chdir('/')
print(os.getcwd())

os.chdir('/Users/btdrew/WorkDocs')
print(os.getcwd())
print(os.path.abspath('test.jpg'))

# some other os commands
print(os.path.dirname('/Users/btdrew/test.jpg'))

print(os.path.basename('/Users/btdrew/test.jpg'))
# check to see if a path exists
print(os.path.exists('/Users/btdrew/test.jpg'))

os.path.isfile
os.path.isdir
os.path.getsize
os.listdir

#so to retrieve a list of all file sizes in a directory..
totalSize = 0
for filename in os.listdir('/Users/btdrew/WorkDocs'):
    if not os.path.isfile(os.path.join('/Users/btdrew/WorkDocs', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('/Users/btdrew/WorkDocs', filename))

print(totalSize)
#create new folders use os.makedirs()