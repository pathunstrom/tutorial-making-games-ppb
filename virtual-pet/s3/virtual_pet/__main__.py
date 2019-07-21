import ppb

from virtual_pet.scenes import Game


def main():
    with ppb.GameEngine(Game) as ge:
        ge.run()


if __name__ == "__main__":
    main()
