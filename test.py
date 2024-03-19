import re
import os
def transport(path, file_name):
    try:
        with open(path, 'r') as file1:
            content = file1.read()
            pattern = r'\b[A-Z][a-z]*\b'
            matches = re.findall(pattern, content)
            with open(file_name, 'w') as file2:
                matches_str = ' '.join(matches)
                file2.write(matches_str)
    except FileNotFoundError:
        print("Error")
path = 'C:\\Users\\kazbe\\OneDrive\\Desktop\\pp2\\test1.txt'
file_name = 'fname.txt'
print(transport(path, file_name))