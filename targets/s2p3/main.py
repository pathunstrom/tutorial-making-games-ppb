import ppb
from ppb import events
from ppb import keycodes


class Player(ppb.BaseSprite):
    position = ppb.Vector(0, 0)
    velocity = ppb.Vector(0, 0)
    speed = 4
    controls = {
        "left": keycodes.A,
        "right": keycodes.D,
    }

    def on_update(self, event: events.Update, signal):
        velocity = self.velocity
        if velocity:
            velocity = self.velocity.scale(self.speed)
        self.position += velocity * event.time_delta

    def on_key_pressed(self, event: events.KeyPressed, signal):
        target_key = event.key
        if target_key == self.controls["left"]:
            self.velocity += ppb.Vector(-self.speed, 0)
        elif target_key == self.controls["right"]:
            self.velocity += ppb.Vector(self.speed, 0)

    def on_key_released(self, event: events.KeyReleased, signal):
        target_key = event.key
        if target_key == self.controls["left"]:
            self.velocity += ppb.Vector(self.speed, 0)
        elif target_key == self.controls["right"]:
            self.velocity += ppb.Vector(-self.speed, 0)


def setup(scene):
    scene.add(Player())


ppb.run(setup)
