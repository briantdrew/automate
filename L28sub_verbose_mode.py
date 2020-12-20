import re
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

#to do a find and replace (substitute) use the sub() method

print(namesRegex.sub('REDACTED','Agent Alice gave the secret documents to Agent Bob.'))

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

# /1 means use group 1 from the match above (\w) which is the A and B

print(namesRegex.sub(r'Agent \1****','Agent Alice gave the secret documents to Agent Bob.'))

#verbose format regular expression strings
# you can spread a long regex across multi[ple lines to make it more readable
# and add comments inside of the regex string per the example.....

re.compile(r'''
(\d\d\d-) |    # area code (without parens, with dash)
(\(\d\d\d\) )  # -or- area code with parens and no dash
\d\d\d    # first 3 digits
-         # second dash
\d\d\d\d
\sx\d{2,4} # extensoion, like x1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE)
# use the pipe | to use multiple valuse in second argument example in line above





