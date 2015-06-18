from pet_class import *

class Cat(Pet):
    def __init__(self):
        super().__init__()
        self.animal = "Cat"

    def feed(self, food):
        if food in self.foods:
            if food == self.foods[0]:
                print("Puur")
                self.hunger -= 5
                self.mood += 1
                self.size += 0.05
                self.energy += 3
            elif food == self.foods[1]:
                print("That's too much for me")
                self.mood -= 1
            elif food == self.foods[2]:
                print("I'm a carnivore")
                self.mood -= 1
            elif food == self.foods[3]:
                print("I don't like fruit")
                self.mood -= 1
            elif food == self.foods[4]:
                print("Are you mad? ")
                self.mood -= 1
            elif food == self.foods[5]:
                print("My favourite")
                self.hunger -= 15
                self.mood += 2
                self.size += 0.15
                self.energy += 15
        else:
            print("I can't eat that")

    def exercise(self, exercise):
        if exercise in self.exercises:
            if exercise == self.exercises[0]:
                self.health += 10
                self.energy -= 10
                self.mood += 1
                self.hunger += 4
                self.xp += 15
                self.size += 0.15
                print("I'm exhausted")
                self.update_level()
            elif exercise == self.exercises[1]:
                print("No way, I despise water")
                self.mood -= 2
            elif exercise == self.exercises[2]:
                self.mood -= 1
                print("I can't cycle")
            elif exercise == self.exercises[3]:
                print("How peaceful")
                self.health += 10
                self.energy -= 5
                self.mood += 1
                self.hunger += 2
                self.xp += 10
                self.size += 0.1
                self.update_level()
            elif exercise == self.exercises[4]:
                print("I climb, not swing")
                self.mood -= 1
        else:
            print("I'm too tired right now")
