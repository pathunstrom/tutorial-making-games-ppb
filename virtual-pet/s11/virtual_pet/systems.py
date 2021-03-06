import json

import ppb

from virtual_pet.events import Aged, GrowsHungry

one_tenth_age = 0.5  # number of seconds to advance age 0.1
hunger_rate = 5  # Rate in seconds to reduce hunger.
food_value = 4


class PetStats(ppb.systems.System):

    def __init__(self, engine, *args, **kwargs):
        try:
            with open("./save_file.json", "r") as save_file:
                data = json.load(save_file)
                self.age = data.get("age", 0)
                self.age_counter = data.get("age_counter", 0)
                self.hunger = data.get("hunger", 10)
                self.hunger_counter = data.get("hunger_counter", 0)
                engine.signal(Aged(self.age))
                engine.signal(GrowsHungry(self.hunger))
        except FileNotFoundError:
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

    def on_quit(self, event, signal):
        data = {
            "age": self.age,
            "age_counter": self.age_counter,
            "hunger": self.hunger,
            "hunger_counter": self.hunger_counter
        }
        with open("./save_file.json", "w") as save_file:
            json.dump(data, save_file)
