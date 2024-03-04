import os

def transport(path ,fname):
    try:
        with open(path, 'r') as file1:
            content = file1.read()
            with open(fname, 'w') as file2:
                file2.write(content)
    except FileNotFoundError:
        print("Error")
path = input("Enter the path: ")
fname = input("Enter the file name: ")
transport(path, fname)