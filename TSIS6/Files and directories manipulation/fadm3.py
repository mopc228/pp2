import os

def d(path):
    if os.path.exists(path):
        print("This path exists.")
        name = os.path.basename(path)
        directory = os.path.dirname(path)
        print("FileName: " + str(name) + ".")
        print("Directory: " + str(directory) + ".")
    else:
        print("This path does not exist.")    

input_path = input("Enter ur path: ")
d(input_path)