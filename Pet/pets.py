from dog_class import *
from cat_class import *


def display_menu():
    print("")
    print("Which type of pet would you like to create? ")
    print("")
    print("1. Dog")
    print("2. Cat")
    print("3. Fish")
    print("4. Monkey")
    print("")
    print("Please select an option from the above menu: ")

def select_option():
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            print("")
            if choice in (1, 2, 3, 4):
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def create_pet():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_pet = Dog()
    elif choice == 2:
        new_pet = Cat()
    elif choice == 3:
        new_pet = Fish()
    elif choice == 4:
        new_pet = Monkey()
    return new_pet

def main():
    new_pet = create_pet()
    manage_pet(new_pet)

if __name__ == "__main__":
    main()

