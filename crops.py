from potato_class import *
from wheat_class import *
from carrot_class import *

def display_menu():
    print("")
    print("Which crop would you like to create? ")
    print("")
    print("1. Potato")
    print("2. Wheat")
    print("3. Carrot")
    print("")
    print("Please select an option from the above menu: ")

def select_option():
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            print("")
            if choice in (1, 2, 3):
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def create_crop():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_crop = Potato()
    elif choice == 2:
        new_crop = Wheat()
    elif choice == 3:
        new_crop = Carrot()
    return new_crop

def main():
    new_crop = create_crop()
    manage_crop(new_crop)

if __name__ == "__main__":
    main()
