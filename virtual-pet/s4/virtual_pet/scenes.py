import ppb

from virtual_pet.sprites import Pet


class Game(ppb.BaseScene):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add(Pet())
