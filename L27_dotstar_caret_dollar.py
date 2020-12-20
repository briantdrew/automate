import re
# caret says must find at beginning of string
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there!'))

# the $ says must find at the end of the string
endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search('It is the end of the world!'))

# use both the caret and dollar sign to find the entire value
#/d+ means 1 or more digits and the caret and dollar mean it has to be that pattern
#all the way through. so if you put an x in the middle, it doesn't work
#take out the x to see it work
allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('234567899x87654321'))

#dot . stand for any single character except new line
#so the next line means anthing at all followed by at
#using findall here to find them all
#the . by itself only find 1 character so use the range to get more
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('That cat in the hat sat on the flat mat.'))

#the .* means 0 or more so = any pattern

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Al Last Name: Sweigart'))

# .* is greedy mode while .*? is non-greedy mode
serve = '<To serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))

greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

# to find any character AND the newline need to use re.DOTALL
prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law'
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime))




