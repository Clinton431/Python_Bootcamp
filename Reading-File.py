
try:
    with open('test.tt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
print(file.closed) 