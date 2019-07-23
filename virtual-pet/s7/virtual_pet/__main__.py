import ppb

from virtual_pet.scenes import Game
from virtual_pet.systems import PetStats


def main():
    with ppb.GameEngine(Game, systems=[PetStats]) as ge:
        ge.run()


if __name__ == "__main__":
    main()
