from pet_class import *

class Dog(Pet):
    def __init__(self):
        super().__init__()
        self.animal = "Dog" 

    def feed(self, food):
        if food in self.food_no:
            if food == self.food_no[0]:
                self.hunger -= 5
                self.mood += 1
                self.size += 0.05
                self.energy += 3
                print("Woof")
                self.update_level()
            elif food == self.food_no[1]:
                self.hunger -= 15
                self.mood += 2
                self.size += 0.2
                self.energy += 10
                print("Mmm meat")
                self.update_level()
            elif food == self.food_no[2]:
                print("I don't like that")
                self.mood -= 1
                self.hunger += 3
                self.update_level()
            elif food == self.food_no[3]:
                print("Go on then")
                self.hunger -= 10
                self.mood += 0.5
                self.size += 0.05
                self.energy += 10
                self.update_level()
            elif food == self.food_no[4]:
                print("That looks disgusting, no way")
                self.mood -= 1
                self.hunger += 5
                self.update_level()
            elif food == self.food_no[5]:
                print("I'm not a cat")
                self.mood -= 1.5
                self.hunger += 5
                self.update_level()
        else:
            print("I don't like that")

    def exercise(self, exercise):
        if exercise in self.ex_no:
            if exercise == self.ex_no[0]:
                self.health += 10
                self.energy -= 5
                self.mood += 2
                self.hunger += 6
                self.xp += 25
                self.size += 0.2
                print("You can't catch me")
                self.update_level()
            elif exercise == self.ex_no[1]:
                self.health += 12
                self.energy -= 7
                self.mood += 1
                self.hunger += 8
                self.xp += 30
                self.size += 0.25
                print("I smell like a wet dog")
                self.update_level()
            elif exercise == self.ex_no[2]:
                print("I can't cycle")
                self.mood -= 0.5
                self.update_level()
            elif exercise == self.ex_no[3]:
                print("Let's go for a stroll")
                self.health += 10
                self.energy -= 5
                self.mood += 2
                self.hunger += 5
                self.xp += 10
                self.size += 0.15
                self.update_level()
            elif exercise == self.ex_no[4]:
                print("I can't swing")
                self.mood -= 0.5
                self.update_level()
        else:
            print("I'm too tired right now")
            

    
