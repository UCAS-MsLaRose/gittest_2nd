# holds user interface, runs the program 
from creater import charCreator

def main():
    choice = input("Select 1 to create a character and 2 to exit")
    if choice == "1":
        charCreator()
    else:
        pass

main()