from pico2d import *
import game_world
import game_framework
from boy import Boy
from ball import Ball
from grass import Grass


def handle_events():
    import item_mode
    import pause_mode
    import title_mode

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.push_mode(item_mode)
        else:
            boy.handle_event(event)



def init():
    global boy


    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)



def update():
    game_world.update()


def clear_projectiles():
    game_world.remove_objects(lambda o: isinstance(o, Ball))


def use_item(number):
    if number == 0:
        clear_projectiles()
    elif number == 1:
        boy.fire_ball(21)
    elif number == 2:
        boy.fire_ball(41)


def render():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    pass


def pause():
    pass


def resume():
    boy.reset_input()


running = True