from math import log1p

import ppb


starting_size = 0.5
max_size = 5


class Pet(ppb.BaseSprite):
    image = "./resources/pet.png"
    size = starting_size

    def on_aged(self, aged_event, signal):
        self.size = min(starting_size * log1p(aged_event.age + 1), max_size)
