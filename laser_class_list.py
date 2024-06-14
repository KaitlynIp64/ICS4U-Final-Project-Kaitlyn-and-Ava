# !/usr/bin/env python3

"""
Created by: Kaitlyn I and Ava V
Created on: June 2024
This is the "LaserList" class
"""

from laser_class import Laser

import constants

class LaserList:
    def __init__(self):
        self.lasers = []

    def add_to_list(self, laser):
        self.clasers.append(laser)

    def fire_laser(self, ship_x_pos: int, ship_y_pos: int, laser_direction: int):
        for laser in self.laser:
            if laser.is_off_screen() == True:
                laser.x_position = ship_x_pos + laser_direction
                laser.y_position = ship_y_pos
                break

    def velocity(self, laser_speed: int) -> None:
        for laser in self.lasers:
            if laser.is_off_screen() == False:
                if laser.is_laser_left_side() == True:
                    laser.x_position -= laser_speed
                else:
                    laser.x_position += laser_speed

    def is_laser_off_screen(self) -> bool:
        for laser in self.lasers:
            if laser.is_off_screen() == False:
                if laser.is_out_of_bounds() == True:
                    laser.move_off_screen()
                    return True
        return False