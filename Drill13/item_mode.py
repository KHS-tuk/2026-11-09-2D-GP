from pico2d import *

import game_framework
import game_world
import play_mode


image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    del image


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    image.draw(400, 300)
    update_canvas()
