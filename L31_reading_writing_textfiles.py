# open a file in read mode
docRead = open('/Users/btdrew/Downloads/lesson31-recap.txt')
content = docRead.read()
print(content)
docRead.close()
docRead = open('/Users/btdrew/Downloads/lesson31-recap.txt')
content = docRead.readlines()
print(content)
docRead.close()
# open in write 'w' or append 'a' mode
# if non-existin file name is used, the file will be created
newFile = open('/Users/btdrew/Downloads/brian.txt', 'w')
#next we can write to it
newFile.write('Hello, my name is Alora')
newFile.close()

baconFile = open('bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable.')

baconFile.close()
import os
print(os.getcwd())
# open in append mode so can add text vs. over writing
baconFile = open('bacon.txt', 'a')
baconFile.write('\n\nBacon is delicious.')
baconFile.close()

# you can store lists and dictionaries and non-text stuff
import shelve
#next line creates mydata.db in /Users/btdrew which is the cwd
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

#can back to the shelf if/when needed
shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile.keys())
keylist = list(shelfFile.keys())
print(keylist)
valueList = list(shelfFile.values())
print(valueList)





