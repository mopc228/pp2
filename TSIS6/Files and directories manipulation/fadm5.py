import os

def transport(name, alist):
    try:
        with open(name, 'w') as file:
            for i in alist:
                file.write(i, "     ")
        print(f"The list has been written to the file '{name}'.")
    except FileNotFoundError:
        print(f"Error")
inp = input("Enter a list: ")
alist = inp.split()
name = input("Enter the file name to write the list: ")
transport(name, alist)
