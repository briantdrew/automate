import re
message = 'call me at 425-555-1234 tomorrow, or at 360-123-4567 at the office'
# added parenthesis in the next line to separate area code from phone number in mo groups
# mo = matched object
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # this is the patter we ae looking for
mo = phoneNumRegex.search(message) # stands for matched object 
# or use findall to find all phone numbers
print(mo.group())
print(phoneNumRegex.findall(message))
print(mo.group(1)) # to print out area code

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

#using ? which means may appear 0 or 1 time
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
#this example makes the area code optional
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 360-123-4567')
print(mo.group())

#using * which means can appear 0 or more times
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search("The Adventures of Batwoman")
print(mo.group())
#and because of the * 
mo = batRegex.search("The Adventures of Batwowowowowowowoman")
print(mo.group())

#using + which means MUST appear at least 1 time, not optional
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search(r'The Adventures of Batman')
#print(mo.group()) # this results in NoneType because woman must be at least 1 time
# this will work

batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search(r'The Adventures of Batman and Batwoman')
print(mo.group())

#to find literals must use escape character with + meaning 1 or more times
regex = re.compile(r'(\+\*\?)+')
mo = regex.search(r'I learned about +*?+*? regex syntax')
print(mo.group())

# find exact number of occurrences using {x}, all are case sensitive
haRegex = re.compile(r'(ha){3}')
mo = haRegex.search('he said hahaha')
print(mo.group())

#finding a complex string which may or may not contain certain elements w/comma optional
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneRegex.search("my numbers are 123-456-5555,555-1212,415-454-2323")
print(mo.group())

# to find a range of occurrences, in this case a range of 3 to 5
haRegex = re.compile(r'(ha){3,5}')
mo = haRegex.search("he said hahahaha")
print(mo.group())

# greedy match (longest match) vs non-greedy match (smallest match)
#the /d says to match digits, in this case between 3 and 5 digits
digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search("1234567890")
print(mo.group()) #prints 12345 which is 'greedy'
#the ? i the next example says to do a non-greedy match
digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('1234567890')
print(mo.group()) # prints 123 which is 'non-greedy'
print(mo.group(1))


phoneNumReg = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumReg.search('my nunmber is (455) 123-4567')
print(mo.group())



