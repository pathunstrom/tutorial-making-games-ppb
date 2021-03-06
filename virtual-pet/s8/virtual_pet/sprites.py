from math import log1p

import ppb


starting_size = 0.5
max_size = 5
hunger_warning_level = 6


class Pet(ppb.BaseSprite):
    image = "./resources/pet.png"
    size = min(starting_size * log1p(1), max_size)

    def on_aged(self, aged_event, signal):
        self.size = min(starting_size * log1p(aged_event.age + 1), max_size)

    def on_grows_hungry(self, hunger_event, signal):
        if hunger_event.hunger <= hunger_warning_level:
            hunger_event.scene.add(Thought(image="./resources/food.png",
                                           position=self.top.right,
                                           size=0.25 * (7 - hunger_event.hunger)))


class Thought(ppb.BaseSprite):
    counter = 0

    def on_update(self, event: ppb.events.Update, signal):
        self.position += ppb.Vector(0, 2) * event.time_delta
        self.counter += event.time_delta
        if self.counter >= 2:  # Lasts two seconds
            event.scene.remove(self)


class Food(ppb.BaseSprite):
    size = 0.5
    image = "./resources/food.png"
    position = ppb.Vector(0, 5)

    def on_update(self, event: ppb.events.Update, signal):
        self.position += ppb.Vector(0, -3) * event.time_delta
        pet = next(event.scene.get(kind=Pet))  # There's only one pet.
        if (pet.position - self.position).length < ((self.size + pet.size) / 2):
            event.scene.remove(self)


class FoodUIButton(ppb.BaseSprite):
    image = "./resources/food-can.png"
    position = ppb.Vector(-5, 4)

    def on_button_pressed(self, button_event: ppb.events.ButtonPressed, signal):
        if (self.left < button_event.position.x < self.right
                and self.top > button_event.position.y > self.bottom):
            button_event.scene.add(Food())
