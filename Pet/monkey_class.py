from pet_class import *

class Monkey(Pet):
    def __init__(self):
        super().__init__()
        self.animal = "Monkey"

    def feed(self, food):
        if food in self.food_no:
            if food == self.food_no[0]:
                self.hunger -= 5
                self.mood += 1
                self.size += 0.05
                self.energy += 5
                print("Oooh oooh aaah aaah")
                self.update_level()
            elif food == self.food_no[1]:
                self.hunger -= 10
                self.mood += 1
                self.size += 0.15
                self.energy += 10
                print("Mmm tasty")
                self.update_level()
            elif food == self.food_no[2]:
                self.mood -= 1
                print("I don't like carrots")
                self.update_level()
            elif food == self.food_no[3]:
                self.mood += 2
                self.energy += 15
                self.hunger -= 15
                self.size += 0.1
                print("My favourite")
                self.update_level()
            elif food == self.food_no[4]:
                self.mood -= 1
                print("I'm not a fish")
                self.update_level()
            elif food == self.food_no[5]:
                self.mood += 0.5
                self.hunger -= 5
                self.energy += 10
                self.size += 0.1
                print("I don't mind a fish")
                self.update_level()
        else:
            print("I don't like that")

    def exercise(self, exercise):
        if exercise in self.ex_no:
            if exercise == self.ex_no[0]:
                print("Sure, I like a jog")
                self.health += 10
                self.energy -= 10
                self.mood += 1
                self.hunger += 5
                self.xp += 20
                self.size += 0.15
                self.update_level()
            elif exercise == self.ex_no[1]:
                self.health += 10
                self.energy -= 5
                self.mood += 1.5
                self.hunger += 8
                self.xp += 30
                self.size += 0.25
                print("The waters freezing!")
                self.update_level()
            elif exercise == self.ex_no[2]:
                print("Most fun")
                self.mood += 1
                self.health += 15
                self.energy -= 15
                self.hunger += 10
                self.xp += 25
                self.size += 0.2
                self.update_level()
            elif exercise == self.ex_no[3]:
                print("It's the right weather for it")
                self.mood += 1
                self.health += 10
                self.energy -= 10
                self.hunger += 5
                self.xp += 25
                self.size += 0.15
                self.update_level()
            elif exercise == self.ex_no[4]:
                print("Right in my environment")
                self.mood += 2
                self.health += 15
                self.energy -= 15
                self.hunger += 10
                self.xp += 30
                self.size += 0.15
                self.update_level()
        else:
            print("I'm too tired right now")
                
