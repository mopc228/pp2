import os

def access(path):
    try:
        if os.path.exists(path):
            print("This path exists.")
        else:
            print("This path does not exist.")
        if os.access(path, os.R_OK):
            print("This path is readible.")
        else:
            print("This path is not readible.")
        if os.access(path, os.W_OK):
            print("This path is writible.")
        else:
            print("This path is not writible")
        if os.access(path, os.X_OK):
            print("This path is executible.")
        else:
            print("This path is not executible.")
    except Exception as e:
        print("Error " + str(e))

input_path = input("Enter your path: ")
access(input_path)