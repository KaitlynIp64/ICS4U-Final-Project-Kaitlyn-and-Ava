# !/usr/bin/env python3

"""
Created by: Kaitlyn I and Ava V
Created on: June 2024
This is the "Ship" class
"""

from images import Images

import constants

class Ship(Images):
    def __init__(self, _x_position: int, _y_position: int):
        super().__init__(_x_position, _y_position)


    def velocity(self, ship_speed: int) -> None:
        self.y_position += ship_speed

    def warp_bottom(self) -> None:
        self.y_position = constants.OFF_BOTTOM_SCREEN

    def warp_top(self) -> None:
        self.y_position = constants.OFF_TOP_SCREEN