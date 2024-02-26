import re

string = input()
r = re.findall('[a-z]+[_][a-z]+', string)
print(r)