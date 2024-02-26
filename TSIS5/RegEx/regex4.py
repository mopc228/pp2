import re

string = input()
r = re.findall('[A-Z][a-z]+', string)
print(r)