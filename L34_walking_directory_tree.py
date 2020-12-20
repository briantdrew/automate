# goal is to walk through a directory tree doing something to most or 
# all files in that entire hierarchy

import os
# the os.walk function is used in for loops and returns 3 values
#   - root folder name, subfolders, filenames) and so makes sense
# to use those as variables..
for folderName, subfolders, filenames in os.walk('/Users/btdrew/Downloads'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()

# some examples of how to use this
for subfolder in subfolders:
    if 'fish' in subfolder:
        os.rmdir(subfolder)

# or
for file in filenames:
    if file.endswith('.py'):
        shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))

