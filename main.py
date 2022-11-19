# -------------------------------------------------- #
# imports

import engine

from engine.handler import scenehandler
from engine.handler.eventhandler import Eventhandler
from engine.misc import clock, user_input, maths
from engine.handler.filehandler import *

from engine.gamesystem import particle
from engine.window import Window

from engine import singleton as EGLOB

# -------------------------------------------------- #
# engine initialization

WINDOW_CAPTION = "Default Title"
WW = 1280
WINDOW_SIZE = [WW, int(WW/16*9)]
WW = 1280//4
FB_SIZE = [WW, int(WW/16*9)]

FPS = 30

Window.create_window(WINDOW_CAPTION, WINDOW_SIZE[0], WINDOW_SIZE[1], pygame.RESIZABLE | pygame.DOUBLEBUF , 16)
# window.set_icon()
fb = Window.create_framebuffer(FB_SIZE[0], FB_SIZE[1], flags=0, bits=32).convert_alpha()

# -------------------------------------------------- #
# ! CHANGE THESE IF YOU WANT !
EGLOB.DEBUG = False
EGLOB.RENDER_DIS = [3, 2]

background = (153, 229, 80)

# -------------------------------------------------- #
# external imports
import random

from scripts.environment import grass

from scripts.game import plant

# -------------------------------------------------- #
# default initializing world

__scene = scenehandler.Scene()
scenehandler.SceneHandler.push_state(__scene)
__layer = __scene.add_layer()
_HANDLER = __layer.handler
_WORLD = __layer.world

# -------------------------------------------------- #
# object initialization

# testing plant

p = plant.Plant("PlantName")

_HANDLER.add_entity(p)

# grass
left = -2
right = 3
grass_count = 5

# left = 0
# right = 1
# grass_count = 300
for x in range(left, right):
    for y in range(left, right):
        GG = grass.GrassHandler("assets/env/grass.json")
        GG.position.xy = (x * EGLOB.CHUNK_PIX_WIDTH, y * EGLOB.CHUNK_PIX_HEIGHT)
        GG.move_to_position()
        GG.calculate_rel_hitbox()
        for i in range(grass_count):
            GG.add_grass(random.randint(0, EGLOB.CHUNK_PIX_WIDTH-GG.assets.get_dimensions(0)[0]//3), random.randint(0, EGLOB.CHUNK_PIX_HEIGHT - GG.assets.get_dimensions(0)[1]//3))
        # print(GG.chunk, GG.p_chunk)
        _WORLD.add_env_obj(GG)

# -------------------------------------------------- #

_HANDLER.handle_changes()
clock.start()
while Window.running:
    if user_input.is_key_pressed(pygame.K_LSHIFT) and user_input.is_key_clicked(pygame.K_d):
        EGLOB.DEBUG = not EGLOB.DEBUG

    # -------------------------------------------------- #
    # update current scene
    if scenehandler.SceneHandler.CURRENT:
        fb.fill(background)
        # update and render
        scenehandler.SceneHandler.CURRENT.update(fb)

    # eventhandler updates
    Eventhandler.update()

    # rescale framebuffer to window
    Window.instance.blit(pygame.transform.scale(fb, (Window.WIDTH, Window.HEIGHT)), (0,0))

    user_input.update()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            Window.running = False
        elif e.type == pygame.KEYDOWN:
            # keyboard press
            user_input.key_press(e)
        elif e.type == pygame.KEYUP:
            # keyboard release
            user_input.key_release(e)
        elif e.type == pygame.MOUSEMOTION:
            # mouse movement
            user_input.mouse_move_update(e)
        elif e.type == pygame.MOUSEBUTTONDOWN:
            # mouse press
            user_input.mouse_button_press(e)
        elif e.type == pygame.MOUSEBUTTONUP:
            # mouse release
            user_input.mouse_button_release(e)
        elif e.type == pygame.WINDOWRESIZED:
            # window resized
            Window.handle_resize(e)
            fbsize = fb.get_size()
            user_input.update_ratio(Window.WIDTH, Window.HEIGHT, fbsize[0], fbsize[1])

    pygame.display.update()
    clock.update()

# -------------------------------------------------- #
# close engine
engine.end()
