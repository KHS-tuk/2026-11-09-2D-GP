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


def handle_events():
    import pause_mode

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key in (SDLK_0, SDLK_1, SDLK_2):
            play_mode.use_item(event.key - SDLK_0)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            continue
        else:
            play_mode.boy.handle_event(event)
