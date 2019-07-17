from dataclasses import dataclass

import ppb
from ppb import events
from ppb import keycodes


class Game(ppb.BaseScene):

    def on_project(self, shoot_event: 'Project', signal):
        self.add(Projectile(position=shoot_event.position))


class Player(ppb.BaseSprite):
    position = ppb.Vector(0, 0)
    velocity = ppb.Vector(0, 0)
    speed = 4
    controls = {
        "left": keycodes.A,
        "right": keycodes.D,
        "project": keycodes.Space,
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
        elif target_key == self.controls["project"]:
            signal(Project(self.top.center))

    def on_key_released(self, event: events.KeyReleased, signal):
        target_key = event.key
        if target_key == self.controls["left"]:
            self.velocity += ppb.Vector(self.speed, 0)
        elif target_key == self.controls["right"]:
            self.velocity += ppb.Vector(-self.speed, 0)


@dataclass
class Project:
    position: ppb.Vector


class Projectile(ppb.BaseSprite):
    velocity = ppb.Vector(0, 8)
    size = 0.25

    def on_update(self, event, signal):
        self.position += self.velocity * event.time_delta
        for target in event.scene.get(kind=Target):
            distance = (target.position - self.position).length
            collision_distance = (target.size + self.size) / 2
            if distance <= collision_distance:
                event.scene.remove(self)
                event.scene.remove(target)
                break
        if self.bottom > 6:
            event.scene.remove(self)


class Target(ppb.BaseSprite):
    pass


def setup(scene):
    scene.add(Player())
    for x in range(-4, 5, 2):
        scene.add(Target(position=ppb.Vector(x, 4)))


ppb.run(setup, starting_scene=Game)
