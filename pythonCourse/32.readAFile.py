
try:
    with open('C:\\Users\\Topalovic\\Desktop\\text.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

