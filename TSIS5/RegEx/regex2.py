import re

string = input()
r = re.match('[a]b{2,3}', string)
print(r)