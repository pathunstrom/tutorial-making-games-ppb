import ppb


def main():
    with ppb.GameEngine(ppb.BaseScene) as ge:
        ge.run()


if __name__ == "__main__":
    main()
