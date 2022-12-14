"""
Plant.py

- Plant object
"""
# -------------------------------------------------- #
# imports

import pygame

from engine.gamesystem.entity import EntityTypes
from engine.graphics import animation
from engine.misc import maths, user_input, clock

from engine.handler import scenehandler
from engine.handler.eventhandler import Event, Eventhandler

from engine import singleton as EGLOB

from scripts import entityext, animationext, singleton

# -------------------------------------------------- #
animation.load_and_parse_aseprite_animation("assets/sprites/default_plant.json")

# -------------------------------------------------- #
# class

class Plant(entityext.GameEntity):
    TYPE = "Plant"

    # -------------------------------------------------- #
    # animations
    ANIM_CAT = "default_plant"
    IDLE_ANIM = "idle"

    # load
    ANIM_CATEGORY = animation.Category.get_category(ANIM_CAT)

    # -------------------------------------------------- #
    # statistics
    MS = 30
    LC = 0.3

    # -------------------------------------------------- #
    # signals
    MOVEMENT_SIGNAL = "Plant-move"

    # wrappers
    MOVEMENT_WRAPPER = Eventhandler.register_to_signal(MOVEMENT_SIGNAL, 
                                                    lambda x: print(x))                   

    # -------------------------------------------------- #
    # buffered objects


    # -------------------------------------------------- #

    def __init__(self, name: str):
        super().__init__(Plant.TYPE if not name else name, 0, 0)
        self.aregist = Plant.ANIM_CATEGORY.create_registry_for_all()
        self.sprite = self.aregist[Plant.IDLE_ANIM].get_frame()
        self.hitbox = self.aregist[Plant.IDLE_ANIM].get_hitbox()
        self.camera = None
    
    def start(self):
        # whatever you want the entity to do before adding to world
        self.camera = self.layer.camera
        self.camera.set_target(self)

    def update(self):
        # update function
        entityext.update_ani_and_hitbox(self, Plant.IDLE_ANIM, handle=False)

        # lerp
        self.motion *= Plant.LC

        # insert movement logic etc
        # movement
        # if user_input.is_key_pressed(pygame.K_d):
        #     self.motion.x += Plant.MS * clock.delta_time
        # if user_input.is_key_pressed(pygame.K_a):
        #     self.motion.x -= Plant.MS * clock.delta_time
        # if user_input.is_key_pressed(pygame.K_w):
        #     self.motion.y -= Plant.MS * clock.delta_time
        # if user_input.is_key_pressed(pygame.K_s):
        #     self.motion.y += Plant.MS * clock.delta_time

        # update entity in world
        self.layer.world.move_entity(self)
        self.move_to_position()
        # update camera
        # self.camera.campos -= self.motion
        # self.camera.track_target()
        # self.camera.update()
        print(self, EGLOB.RENDER_DIS)
    
    def render(self, surface):
        # render function
        surface.blit(self.sprite if self.motion.x < 0 else pygame.transform.flip(self.sprite, True, False), 
                    self.camera.get_target_rel_pos())

    def debug(self, surface):
        # debug function
        super().debug(surface)
        # any addition rendering you want
    
    def __repr__(self) -> str:
        return f"Plant: {self.name} | Id: {self.id}"

# -------------------------------------------------- #
# setup
EntityTypes.register_entity_type(Plant.TYPE, Plant)



