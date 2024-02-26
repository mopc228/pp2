import re

def splitting(s):
    result = re.split('(?=[A-Z])', s)
    return result

s = input()
result_list = splitting(s)
result_string = ' '.join(result_list)
print(result_string)
