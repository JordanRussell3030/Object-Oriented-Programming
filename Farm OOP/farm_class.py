from animals import *
from crops import *

def display_menu():
    print("")
    print("Welcome to the farm simulator")
    print("")
    print("Which section of the farm would you like to manage? ")
    print("")
    print("1. Animals")
    print("2. Crops")
    print("")
    print("Please select a section")

def get_option():
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            print("")
            if choice in (1, 2):
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def run_simulation():
    display_menu()
    choice = get_option()
    if choice == 1:
        new_animal = create_animal()
        manage_animal(new_animal)
        return new_animal
    elif choice == 2:
        new_crop = create_crop()
        manage_crop(new_crop)
        return new_crop

def main():
    run_simulation()

if __name__ == "__main__":
    main()
