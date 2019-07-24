import ppb

from virtual_pet.events import Aged, GrowsHungry

one_tenth_age = 0.5  # number of seconds to advance age 0.1
hunger_rate = 5  # Rate in seconds to reduce hunger.
food_value = 4


class PetStats(ppb.systems.System):

    def __init__(self, *args, **kwargs):
        self.age = 0
        self.age_counter = 0

        self.hunger = 10
        self.hunger_counter = 0

    def on_update(self, event: ppb.events.Update, signal):

        self.age_counter += event.time_delta
        if self.age_counter >= one_tenth_age:
            self.age += 0.1
            self.age_counter -= one_tenth_age
            signal(Aged(self.age))
        self.hunger_counter += event.time_delta
        if self.hunger_counter >= hunger_rate:
            self.hunger -= 1
            self.hunger_counter -= hunger_rate
            signal(GrowsHungry(self.hunger))

    def on_render(self, event, signal):
        print(self.age)
        print(self.hunger)

    def on_food_eaten(self, event, signal):
        self.hunger += food_value