from pet_class import *

class Fish(Pet):
    def __init__(self):
        super().__init__()
        self.animal = "Fish"

    def feed(self, food):
        if food in self.food_no:
            if food == self.food_no[0]:
                self.hunger -= 5
                self.mood += 1
                self.size += 0.05
                self.energy += 3
                print("Glub Glub")
                self.update_level()
            elif food == self.food_no[1]:
                self.mood += 1
                self.hunger -= 10
                self.size += 0.15
                self.energy += 10
                print("Krabby patty!")
                self.update_level()
            elif food == self.food_no[2]:
                print("I don't like that")
                self.mood -= 1
                self.hunger += 3
                self.update_level()
            elif food == self.food_no[3]:
                print("I don't like that")
                self.mood -= 1
                self.hunger += 3
                self.update_level()
            elif food == self.food_no[4]:
                print("Fantastic")
                self.mood += 1
                self.size += 0.5
                self.hunger -= 5
                self.energy += 5
                self.update_level()
            elif food == self.food_no[5]:
                print("I'm not a cannibal!")
                self.mood -= 2
                self.hunger += 5
                self.update_level()
        else:
            print("I don't like that")

    def exercise(self, exercise):
        if exercise in self.ex_no:
            if exercise == self.ex_no[0]:
                print("I can't stand, I'm a fish")
                self.mood -= 1
                self.update_level()
            elif exercise == self.ex_no[1]:
                self.health += 10
                self.energy -= 5
                self.mood += 1.5
                self.hunger += 8
                self.xp += 30
                self.size += 0.25
                print("Right in my comfort zone")
                self.update_level()
            elif exercise == self.ex_no[2]:
                print("I can't cycle")
                self.mood -= 0.5
                self.update_level()
            elif exercise == self.ex_no[3]:
                print("I can't stand, I'm a fish")
                self.mood -= 1
                self.update_level()
            elif exercise == self.ex_no[4]:
                print("I can't swing")
                self.mood -= 0.5
                self.update_level()
        else:
            print("I'm too tired right now")
