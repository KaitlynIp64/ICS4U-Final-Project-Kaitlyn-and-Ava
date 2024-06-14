#!/usr/bin/env python3

# Created by: Kaitlyn I and Ava V
# Created on: June 2024
# This constants file is for Space Alien game

from ship_class import Ship
from laser_class import Laser
from laser_class_list import LaserList
from alien_class import Alien
from alien_class_list import AlienList

import random
import time
import constants
import stage
import supervisor
import ugame


def splash_scene():
    """
    This function is the splash_scene
    """

    # get sound ready
    coin_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    # sound.play(coin_sound)

    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    
    # used this program to split the image into tile: 
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]
    game.render_block()

    # game loop
    while True:
        time.sleep(2.0)
        menu_scene()


def menu_scene():
    """
    this function is the menu_scene
    """

    image_bank = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text = []
    text1 = stage.Text(width=29, height=12, font=None, buffer=None)
    text1.move(10, 10)
    text1.text("ALIEN SHOOTER")
    text.append(text1)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()

    # game loop
    while True:
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_START != 0:
            game_scene()

        if keys & ugame.K_SELECT != 0:
            game_rules_scene()

        game.tick()

def game_scene():
    """
    this function is the game_scene
    """
    
    # for score
    score = 0
    
    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew.wav", "rb")
    boom_sound = open("boom.wav", "rb")
    crash_sound = open("crash.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # create ship object
    ship = stage.Sprite(
        image_bank_sprites,
        5,
        75,
        constants.SCREEN_Y - (2 * constants.SPRITE_SIZE),
    )
    
    # create alien object(s)
    # ** need to change image bank numbers
    aliens = []
    alien_objects = AlienList()

    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites, 8, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        aliens.append(a_single_alien)
        a_alien_object = Alien(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y, "right")
        alien_objects.add_to_list(a_alien_object)
    
    # place 2 aliens on the screen
    alien_objects.spawn_alien_right()
    alien_objects.spawn_alien_left()
    
    # create laser object(s)
    lasers = []
    laser_objects = LaserList()

    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 2, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)

        a_laser_object = Laser(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        laser_objects.add_to_list(a_laser_object)

    game = stage.Stage(ugame.display, 60)
    game.layers = [score_text] + aliens + [ship] + lasers + [background]
    game.render_block()

    # game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_X:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        if keys & ugame.K_O:
            if b_button == constants.button_state["button_up"]:
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
        else:
            if b_button == constants.button_state["button_still_pressed"]:
                b_button = constants.button_state["button_released"]
            else:
                b_button = constants.button_state["button_up"]

        if keys & ugame.K_UP:
            if ship.y > constants.OFF_TOP_SCREEN:
                ship_object.velocity(-constants.SHIP_SPEED)
                ship.move(ship_object.x_pos, ship_object.y_pos)
            else:
                ship_object.warp_bottom()
                ship.move(ship_object.x_pos, ship_object.y_pos)

        if keys & ugame.K_DOWN:
            if ship.y < constants.OFF_BOTTOM_SCREEN:
                ship_object.velocity(constants.SHIP_SPEED)
                ship.move(ship_object.x_pos, ship_object.y_pos)
            else:
                ship_object.warp_top()
                ship.move(ship_object.x_pos, ship_object.y_pos)

        # Update the position of each sprite based on the corresponding lasers object
        for laser_counter, laser in enumerate(laser_objects.lasers):
            lasers[laser_counter].move(laser.x_pos, laser.y_pos)

        for alien_counter, alien in enumerate(alien_objects.aliens):
            aliens[alien_counter].move(alien.x_pos, alien.y_pos)

        # update game logic
        if a_button == constants.button_state["button_just_pressed"]:
            laser_objects.fire_laser(ship_object.x_pos, ship_object.y_pos, -1)

        if b_button == constants.button_state["button_just_pressed"]:
            laser_objects.fire_laser(ship_object.x_pos, ship_object.y_pos, 1)
        
        laser_objects.velocity(constants.LASER_SPEED)

        alien_objects.velocity(constants.ALIEN_SPEED)

        if laser_objects.is_laser_off_screen():
            score -= 1
            if score < 0:
                score = 0
            score_text.clear()
            score_text.cursor(0, 0)
            score_text.move(1, 1)
            score_text.text(f"Score: {score:.0f}")

        if alien_objects.is_laser_colliding(laser_objects):
            # sound.stop()
            # sound.play(boom_sound)
            score += 1
            score_text.clear()
            score_text.cursor(0, 0)
            score_text.move(1, 1)
            score_text.text(f"Score: {score:.0f}")

        if ship_objects.is_ship_colliding(ship_object):
            # sound.stop()
            # sound.play(boom_sound)
            time.sleep(2.0)
            game_over_scene(score)

        # redraw sprites
        game.render_sprites(aliens + [ship] + lasers)
        game.tick()


def game_over_scene(final_score: int):
    # this function is the game over scene

    # turn off sound from last scene
    sound = ugame.audio
    sound.stop()

    # image banks for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # set the background to image 0 in the image bank
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # add text objects
    text = []

    text1 = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(10, 10)
    text1.text("GAME OVER")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text2.move(10, 90)
    text2.text(f"FINAL SCORE: {final_score:.0f}")
    text.append(text2)

    text3 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text3.move(10, 110)
    text3.text("START: reload game")
    text.append(text3)

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set all layers of all sprites, items show up in order
    game.layers = text + [background]

    # render all sprites
    # most likely you will only render the background once per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # wait for 2 seconds
        keys = ugame.buttons.get_pressed()

        # get user input
        if keys & ugame.K_START != 0:
            supervisor.reload()

        # update game logic
        game.tick()  # wait until refresh rate finishes

if __name__ == "__main__":
    splash_scene()