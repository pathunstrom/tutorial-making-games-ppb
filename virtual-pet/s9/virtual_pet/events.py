from dataclasses import dataclass


@dataclass
class Aged:
    age: float


@dataclass
class GrowsHungry:
    hunger: float


@dataclass
class FoodEaten:
    '''This is just a message, it doesn't need any parameters.'''
    pass
