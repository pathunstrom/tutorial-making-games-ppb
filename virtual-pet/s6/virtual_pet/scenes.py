

import ppb

from virtual_pet.sprites import Pet


starting_size = 0.25
max_size = 5


class Game(ppb.BaseScene):
    size = starting_size

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add(Pet())
