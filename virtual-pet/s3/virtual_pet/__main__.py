import ppb


def main():
    with ppb.GameEngine(ppb.BaseSprite) as ge:
        ge.run()


if __name__ == "__main__":
    main()
