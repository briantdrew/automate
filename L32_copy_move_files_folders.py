import shutil
# to copy a file from one folder to another
shutil.copy('/Users/btdrew/bacon.txt', '/Users/btdrew/Desktop/bacon.txt')
# to copy and rename the file, just provide new name
shutil.copy('/Users/btdrew/bacon.txt', '/Users/btdrew/Desktop/baconandeggs.txt')
# copy a folder of folders aka. directory tree
#shutil.copytree('/Users/btdrew/WorkDocs/test', '/Users/btdrew/WorkDocs/test2')

# to move a file to a new location - does not copy but rather relocates
shutil.move('test.jpg', '/Users/btdrew/Desktop')
# or move to same folder with new name same as renaming a file