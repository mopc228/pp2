import re
string = input()
r = re.match('[a]b*', string)
print(r)