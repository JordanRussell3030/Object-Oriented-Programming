import random

class GenericCrop:
    """A generic food crop"""
    def __init__(self, growth_rate, light_need, water_need):
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

    def  needs(self):
        return {"Light need":self._light_need, "Water need":self._water_need}

    def report(self):
        return {"Growth":self._growth, "Days growing":self._days_growing, "Status":self._status, "Type":self._type}

    def _update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self.status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seed"
        
    def grow(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            self._growth = self._growth + self._growth_rate
        self._days_growing = self._days_growing + 1
        self._update_status()

def auto_grow(crop, days):
    for day in range(days):
        light = random.randint(1, 10)
        water = random.randint(1, 10)
        crop.grow(light, water)

def manual_grow(crop):
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a light value between 1 and 10: "))
            if 1 <= light <= 10:
                valid = True
            else:
                print("Value entered is not valid - please enter another value between 1 and 10")
        except ValueError:
            print("Value entered is not valid - please enter another value between 1 and 10")
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
    crop.grow(light, water)

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

def manage_crop(crop):
    print("This is the crop management program")
    print("")
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print("")
        if option == 1:
            manual_grow(crop)
        elif option == 2:
            auto_grow(crop, 30)
            print("")
        elif option == 3:
            print(crop.report())
            print("")
        elif option == 0:
            noexit = False
            print("")
    print("Thank you for using the crop management program")
        
def main():
    new_crop = GenericCrop(1, 4, 3)
    manage_crop(new_crop)
          
if __name__ == "__main__":
    main()
