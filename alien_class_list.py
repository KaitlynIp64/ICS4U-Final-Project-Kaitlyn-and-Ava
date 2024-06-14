# !/usr/bin/env python3

"""
Created by: Kaitlyn I and Ava V
Created on: June 2024
This is the "Alien List" class
"""

from alien_class import Alien

import constants
import random
import stage
import ugame

class AlienList:
    def __init__(self):
        self.aliens = []

    def add_to_list(self, alien):
        self.aliens.append(alien)

    def spawn_alien(self):
        random_side = random.choice(["right", "left"])
        if random_side == "right":
            self.spawn_alien_right()
        else:
            self.spawn_alien_left()

    def spawn_alien_right(self):
        for alien in self.aliens:
            if not alien.is_alien_left_side():
                if alien.is_off_screen():
                    alien.x_position = constants.OFF_RIGHT_SCREEN
                    alien.y_position = random.randint(0, (constants.SCREEN_Y - constants.SPRITE_SIZE))
                    break

    def spawn_alien_left(self):
        for alien in self.aliens:
            if alien.is_alien_left_side():
                if alien.is_off_screen():
                    alien.x_position = constants.OFF_LEFT_SCREEN
                    alien.y_position = random.randint(0, (constants.SCREEN_Y - constants.SPRITE_SIZE))
                    break

    def velocity(self, alien_speed: int) -> None:
        for alien in self.aliens:
            if not alien.is_off_screen():
                if not alien.is_alien_left_side():
                    alien.x_position -= alien_speed
                elif alien.is_alien_left_side():
                    alien.x_position += alien_speed

                if alien.is_out_of_bounds():
                    alien.move_off_screen()
                    self.spawn_alien()

    def is_laser_colliding(self, laser_objects) -> bool:
        game = stage.Stage(ugame.display, 60)
        for laser in laser_objects.lasers:
            for ship in self.ships:
                if (not laser.is_off_screen() and not ship.is_off_screen() and
                    stage.collide(
                        laser.x_pos + 4, laser.y_pos + 4, laser.x_pos + 12, laser.y_pos + 12,
                        alien.x_pos, alien.y_pos, alien.x_pos + 16, alien.y_pos + 16,
                    )
                ):
                    laser.move_off_screen()
                    alien.move_off_screen()
                    self.spawn_alien()
                    self.spawn_alien()
                    return True
        return False

    def is_alien_colliding(self, alien_object) -> bool:
        game = stage.Stage(ugame.display, 60)
        for alien in self.aliens:
            if (not alien.is_off_screen() and
                stage.collide(
                alien.x_pos + 1, alien.y_pos + 1, alien.x_pos + 15, alien.y_pos + 15,
                alien_object.x_pos + 6, alien_object.y_pos + 3, alien_object.x_pos + 10, alien_object.y_pos + 13,
                )
            ):
                return True
        return False