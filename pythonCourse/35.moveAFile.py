import os

source = "C:\\Users\\Topalovic\\Desktop\\text.txt"
destination = "C:\\Users\\Topalovic\\Desktop\\New Folder\\text.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")