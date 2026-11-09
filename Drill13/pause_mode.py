from pico2d import *
import game_framework
import game_world

font = None


def init():
    global font
    font = load_font('C:/Windows/Fonts/malgun.ttf', 36)


def finish():
    global font
    del font


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    font.draw(300, 360, 'PAUSED', (255, 255, 0))
    font.draw(235, 300, 'Press P to resume', (255, 255, 255))
    update_canvas()


def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()
