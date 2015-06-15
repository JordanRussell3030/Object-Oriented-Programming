class VirtualPet:
    def __init__(self):
        self.name = None
        self.size = 0
        self.age = 0
        self.energy = 50
        self.mood = 5
        self.fat = 5
        print("I have been born")
        self.foods = ["Chicken", "Raspberries", "Bread"]
        self.exercises = ["Walk", "Run", "Swim", "Lift", "Roll"]

    def eat(self, food):
        if food in self.foods:
            if food == self.foods[0]:
                print("Top")
                self.energy = self.energy + 25
                self.mood = self.mood + 5
            elif food == self.foods[1]:
                print("Cheers")
                self.energy = self.energy + 15
                self.mood = self.mood + 1
            elif food == self.foods[2]:
                print("Mmmmm")
                self.energy = self.energy + 20
                self.mood = self.mood + 2
        else:
            print("No thanks")

    def exercise(self, exercise):
        if exercise in self.exercises:
            if exercise == self.exercises[0]:
                self.size = self.size + 0.5
                self.fat = self.fat - 0.25
                self.energy = self.energy - 3
                self.mood = self.mood + 1
                print("Wonderful weather we're having")
            elif exercise == self.exercises[1]:
                self.size = self.size + 0.75
                self.fat = self.fat - 0.45
                self.energy = self.energy - 7
                self.mood = self.mood + 2
                print("I'm worn out now")
            elif exercise == self.exercises[2]:
                self.size = self.size + 0.8
                self.fat = self.fat - 0.65
                self.energy = self.energy - 4
                self.mood = self.mood + 3
                print("Refreshing")
            elif exercise == self.exercises[3]:
                self.size = self.size + 0.6
                self.fat = self.fat - 0.3
                self.energy = self.energy - 2
                self.mood = self.mood + 2
                print("Do you even lift? ")
            elif exercise == self.exercises[4]:
                self.energy = self.energy - 0.1
                self.mood = self.mood + 3
                print("That was fun")
        else:
            print("I can't be bothered")

pet_one = VirtualPet()

pet_one.name = input("What would you like to name your pet? ")

print(pet_one.name)

pet_one.eat("Chicken")
print(pet_one.name)
print(pet_one.energy)
print(pet_one.mood)
pet_one.exercise("Lift")
print(pet_one.name)
print(pet_one.size)
print(pet_one.fat)
print(pet_one.energy)
print(pet_one.mood)


print("('{@} < {@}')")
