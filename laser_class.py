# !/usr/bin/env python3

"""
Created by: Kaitlyn I and Ava V
Created on: June 2024
This is the "Laser" class
"""

from images import Images

import constants

class Laser(Images):
    def __init__(self, _x_position: int, _y_position: int):
        super().__init__(_x_position, _y_position)


    def is_laser_left_side(self) -> bool:
        return self.x_position < 74