import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex)
#findall searches for all matches of the regular expression pattern
#first populate some data to search through, normally would be a file or DB
resume = ''' Brian Drew, Cell: 508-555-5555, Home: 123-543-8759'''

print(phoneRegex.findall(resume))

# if use groups in the reg expression - noted by paranthesis
phoneRegex = re.compile(' (\d\d\d)-(\d\d\d-\d\d\d\d)')
# the result will a list of tuples, each of which has a list of stirngs
print(phoneRegex.findall(resume))

#another version using 3 groups:
phoneRegex = re.compile(' ((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(resume))

lyrics = ''' 1 partridge in a pear tree, 2 turtle doves, 3 french hens,
4 calling birds, 5 gold rings, 6 geese a-laying, 7 swans a-swimming, 
8 maids a-milking, 9 ladies dancing, 10 lords a-leaping, 11 pipers piping, 
12 drummers drumming. '''

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

#we can also create our own character class like \d \s \w above
#we'll call it vowelRegex and the chacater class = aeiouAEIOU
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall(lyrics))

print(vowelRegex.findall('robocop eats baby food.'))

# to use the negative of a character class use the ^ in front of it
# aka does the opposite
vowelRegex = re.compile(r'[^aeiouAEIOU]') #means what ever is NOT aeiouAEIOU
print(vowelRegex.findall(lyrics))
#another example of the negative character class
print(vowelRegex.findall('robocop eats baby food.'))
