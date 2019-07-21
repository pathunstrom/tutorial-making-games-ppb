import ppb

from virtual_pet.events import Aged

one_tenth_age = 0.5  # number of seconds to advance age 0.1


class PetStats(ppb.systems.System):

    def __init__(self, *args, **kwargs):
        self.age = 0
        self.age_counter = 0

    def on_update(self, event: ppb.events.Update, signal):

        self.age_counter += event.time_delta
        if self.age_counter >= one_tenth_age:
            self.age += 1
            self.age_counter -= one_tenth_age
            signal(Aged(self.age))

    def on_render(self, event, signal):
        print(self.age)
