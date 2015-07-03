from animal_class import *

class Cow(GenericAnimal):
    def __init__(self, growth_rate, food_need, water_need):
        super().__init__(1, 4, 6)
        self._type = "Cow"

        def feed(self, food, water):
            if food >= self._food_need and water >= self._water_need:
                self._weight = self._weight + self._growth_rate
        self._days_growing += 1
        self._update_status()
