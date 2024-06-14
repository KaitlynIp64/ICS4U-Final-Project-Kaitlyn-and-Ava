# !/usr/bin/env python3

"""
Created by: Kaitlyn I and Ava V
Created on: June 2024
This is the "images" class
"""

import constants

class Images:
    def __init__(self, _x_position: int, _y_position: int):
        self.x_position = _x_position
        self.y_position = _y_position

    # Getter for x_position
    @property
    def x_pos(self) -> int:
        return self.x_position

    # Getter for y_position
    @property
    def y_pos(self) -> int:
        return self.y_position

    # Setter for x_position
    @x_pos.setter
    def x_pos(self, value: int):
        self.x_position = value

    # Setter for y_position
    @y_pos.setter
    def y_pos(self, value: int):
        self.y_position = value


    def velocity(self, object_speed: int) -> None:
        self.x_position += object_speed

    def is_off_screen(self) -> bool:
        return self.y_position == constants.OFF_SCREEN_Y

    def is_out_of_bounds(self) -> bool:
        return (self.x_position > constants.SCREEN_X) or (self.x_position < -16)

    def move_off_screen(self):
        self.x_position = constants.OFF_SCREEN_X
        self.y_position = constants.OFF_SCREEN_Y