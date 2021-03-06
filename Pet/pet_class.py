import time

class Pet:
    """A virtual pet"""
    def __init__(self):
        self.name = None
        self.health = 50
        self.energy = 50
        self.mood = 5
        self.hunger = 50
        self.xp = 0
        self.level = 1
        self.size = 1
        self.animal = "Default Pet"
        self.foods = ["Biscuit", "Burger", "Carrot", "Banana", "Fish food", "Fish"]
        self.exercises = ["Run", "Swim", "Cycle", "Walk", "Swing"]
        self.food_no = ["1", "2", "3", "4", "5", "6"]
        self.ex_no = ["1", "2", "3", "4", "5"]

    def feed(self, food):
        if food in self.food_no:
            if food == self.food_no[0]:
                self.hunger -= 10
                self.mood += 0.5
                self.size += 0.05
                self.energy += 5
                print("Crunchy")
                self.update_level()
            elif food == self.food_no[1]:
                self.hunger -= 25
                self.mood += 1
                self.size += 0.15
                self.energy += 7
                print("My favourite")
                self.update_level()
            elif food == self.food_no[2]:
                self.hunger -= 15
                self.mood += 0.2
                self.size += 0.01
                self.energy += 8
                print("I hate vegetables")
                self.update_level()
            elif food == self.food_no[3]:
                self.hunger -= 20
                self.mood += 1.5
                self.size += 0.1
                self.energy += 6
                print("Full of potassium")
                self.update_level()
            elif food == self.food_no[4]:
                self.hunger -= 5
                self.mood += 0.5
                self.size += 0.05
                self.energy += 2
                print("Not my favourite, but ok")
                self.update_level()
            elif food == self.food_no[5]:
                self.hunger -= 15
                self.mood += 1
                self.size += 0.1
                self.energy += 4
                self.update_level()
        else:
            print("I can't eat that")

    def exercise(self, exercise):
        if exercise in self.ex_no:
            if exercise == self.ex_no[0]:
                self.health += 10
                self.energy -= 10
                self.mood += 1
                self.hunger += 5
                self.xp += 10
                self.size += 0.25
                print("I'm getting faster")
                self.update_level()
            elif exercise == self.ex_no[1]:
                self.health += 15
                self.energy -= 15
                self.mood += 2
                self.hunger += 7
                self.xp += 15
                self.size += 0.3
                print("I love to swim")
                self.update_level()
            elif exercise == self.ex_no[2]:
                self.health += 12
                self.energy -= 12
                self.mood += 1.5
                self.hunger += 8
                self.xp += 10
                self.size += 0.2
                print("I enjoy cycling")
                self.update_level()
            elif exercise == self.ex_no[3]:
                self.health += 5
                self.energy -= 5
                self.mood += 2
                self.hunger += 4
                self.xp += 10
                self.size += 0.1
                print("A nice stroll in the countryside")
                self.update_level()
            elif exercise == self.ex_no[4]:
                self.health += 7
                self.energy -= 7
                self.mood += 1
                self.hunger += 5
                self.xp += 15
                self.size += 0.15
                print("Swinging through the trees")
                self.update_level()
        else:
            print("I'm too tired for that")

    def pet_name(self):
        return {"Name":self.name, "Animal":self.animal}

    def stats(self):
        return {"Health":self.health, "Energy":self.energy, "Hunger":self.hunger, "Mood":self.mood, "Size":round(self.size)}

    def pet_level(self):
        return {"XP":self.xp, "Level":self.level}

    def update_level(self):
        if self.xp >= 100:
            self.level += 1
            self.xp = 0
        if self.mood <= 0:
            print("You have neglected your pet and it ran away.")
            time.sleep(5)
            quit()
        elif self.mood >= 10:
            self.mood = 10
        if self.health <= 0:
            print("Your pet has died")
            time.sleep(5)
            quit()
        elif self.health >= 100:
            self.health = 100
        if self.energy <= 0:
            print("Your pet has died")
            time.sleep(5)
            quit()
        elif self.energy >= 100:
            self.energy = 100
        if self.hunger >= 100:
            print("Your pet has starved to death")
            time.sleep(5)
            quit()
        elif self.hunger <= 0:
            self.hunger = 0
        if self.size >= 10:
            self.size = 10
        

def display_menu():
    print("")
    print("1. Feed your pet")
    print("2. Exercise your pet")
    print("3. Display your pets stats")
    print("0. Exit program")
    print("")
    print("Please select an option from the above menu")

def get_menu_choice():
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            if 0<= choice <= 3:
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def display_food():
    foods = ["Biscuit", "Burger", "Carrot", "Banana", "Fish food", "Fish"]
    food_no = ["1", "2", "3", "4", "5", "6"]
    print("")
    print("Food list: ")
    print("")
    for index, food in enumerate(foods):
        print("{0}. {1}".format(index + 1, food))
    
def display_exercises():
    exercises = ["Run", "Swim", "Cycle", "Walk", "Swing"]
    ex_no = ["1", "2", "3", "4", "5"]
    print("")
    print("Exercise list: ")
    print("")
    for index, exercise in enumerate(exercises):
        print("{0}. {1}".format(index + 1, exercise))

def manage_pet(pet):
    print("This is the pet training program")
    print("")
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print("")
        if option == 1:
            display_food()
            print("")
            food = input("What would you like to feed your pet? ")
            print("")
            pet.feed(food)
        elif option == 2:
            display_exercises()
            print("")
            exercise = input("How would you like to exercise your pet? ")
            print("")
            pet.exercise(exercise)
        elif option == 3:
            print(pet.pet_name())
            print(pet.stats())
            print(pet.pet_level())
        elif option == 0:
            noexit = False
            print("Thanks for playing")
            quit()
    
def main():
    new_pet = Pet()
    manage_pet(new_pet)

if __name__ == "__main__":
    main()
        
        
