import os

def way(path):
    try:
        entries = os.listdir(path)
        
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print("Error: The specified path " + str(path) + " does not exist")
path_input = input("Enter the path: ")
way(path_input)