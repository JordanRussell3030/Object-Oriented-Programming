import random

class GenericAnimal:
    """A generic animal"""
    def __init__(self, growth_rate, food_need, water_need):
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Baby"
        self._type = "Generic"
        self._name = None

    def needs(self):
        return {"Food need":self._food_need, "Water need":self._water_need}

    def report(self):
        return {"Type":self._type, "Status":self._status, "Weight":self._weight, "Days growing":self._days_growing}

    def _update_status(self):
        if self._weight > 15:
            self._status = "Meat grinder"
        elif self._weight > 10:
            self._status = "Plump"
        elif self._weight > 5:
            self.status = "Young"
        elif self._weight > 0:
            self._status = "Baby"
        elif self._weight == 0:
            self._status = "Newborn"

    def feed(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            self._weight = self._weight + self._growth_rate
        self._days_growing += 1
        self._update_status()

def auto_feed(animal, days):
    for day in range(days):
        food = random.randint(1, 10)
        water = random.randint(1, 10)
        animal.feed(food, water)

def manual_feed(animal):
    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value between 1 and 10: "))
            if 1 <= food <= 10:
                valid = True
            else:
                print("Value entered is not valid - please enter another value between 1 and 10")
        except ValueError:
            print("Value entered is not valid - please enter another value between 1 and 10 ")
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value between 1 and 10: "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered is invalid - please enter another value between 1 and 10")
        except ValueError:
            print("Value entered is invalid - please enter another value between 1 and 10")
    animal.feed(food, water)

def display_menu():
    print("")
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit test program")
    print("")
    print("Please select an option from the above menu")

def get_menu_choice():
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            if 0 <= choice <= 3:
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def manage_animal(animal):
    print("This is the animal management program")
    print("")
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print("")
        if option == 1:
            manual_feed(animal)
        elif option == 2:
            auto_feed(animal, 30)
            print("")
        elif option == 3:
            print(animal.report())
            print("")
        elif option == 0:
            noexit = False
            print("")
    print("Thank you for using the crop management program")
        
def main():
    new_animal = GenericAnimal(1, 4, 3)
    manage_animal(new_animal)
          
if __name__ == "__main__":
    main()
