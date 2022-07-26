import re

# List of patterns to search for

# Text to parse
text = 'This is a string with term1.'
if re.search("term[0-4]",  text):
        print('Found first term.')
if re.search("term[5-9]",  text):
        print ('Found second term.')