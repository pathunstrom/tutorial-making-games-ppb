import ppb


class Player(ppb.BaseSprite):
    position = ppb.Vector(0, 0)
    velocity = ppb.Vector(0, 0)
    speed = 4


def setup(scene):
    scene.add(Player())


ppb.run(setup)
