from pet_class import *

class Cat(Pet):
    def __init__(self):
        super().__init__()
        self.animal = "Cat"

    def feed(self, food):
        if food in self.food_no:
            if food == self.food_no[0]:
                print("Puur")
                self.hunger -= 5
                self.mood += 1
                self.size += 0.05
                self.energy += 3
                self.update_level()
            elif food == self.food_no[1]:
                print("That's too much for me")
                self.mood -= 1
                self.update_level()
            elif food == self.food_no[2]:
                print("I'm a carnivore")
                self.mood -= 1
                self.update_level()
            elif food == self.food_no[3]:
                print("I don't like fruit")
                self.mood -= 1
                self.update_level()
            elif food == self.food_no[4]:
                print("Are you mad? ")
                self.mood -= 1
                self.update_level()
            elif food == self.food_no[5]:
                print("My favourite")
                self.hunger -= 15
                self.mood += 2
                self.size += 0.15
                self.energy += 15
                self.update_level()
        else:
            print("I can't eat that")

    def exercise(self, exercise):
        if exercise in self.ex_no:
            if exercise == self.ex_no[0]:
                self.health += 10
                self.energy -= 10
                self.mood += 1
                self.hunger += 4
                self.xp += 15
                self.size += 0.15
                print("I'm exhausted")
                self.update_level()
            elif exercise == self.ex_no[1]:
                print("No way, I despise water")
                self.mood -= 2
                self.update_level()
            elif exercise == self.ex_no[2]:
                self.mood -= 1
                print("I can't cycle")
                self.update_level()
            elif exercise == self.ex_no[3]:
                print("How peaceful")
                self.health += 10
                self.energy -= 5
                self.mood += 1
                self.hunger += 2
                self.xp += 10
                self.size += 0.1
                self.update_level()
            elif exercise == self.ex_no[4]:
                print("I climb, not swing")
                self.mood -= 1
                self.update_level()
        else:
            print("I'm too tired right now")
