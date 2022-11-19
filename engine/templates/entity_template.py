"""
template.py

- template object
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
animation.load_and_parse_aseprite_animation("insert/file/path")

# -------------------------------------------------- #
# class

class Template(entityext.GameEntity):
    TYPE = "Template"

    # -------------------------------------------------- #
    # animations
    ANIM_CAT = "template"
    IDLE_ANIM = "idle"

    # load
    ANIM_CATEGORY = animation.Category.get_category(ANIM_CAT)

    # -------------------------------------------------- #
    # statistics
    MS = 30
    LC = 0.3

    # -------------------------------------------------- #
    # signals
    MOVEMENT_SIGNAL = "template-move"

    # wrappers
    MOVEMENT_WRAPPER = Eventhandler.register_to_signal(MOVEMENT_SIGNAL, 
                                                    lambda x: print(x))                   

    # -------------------------------------------------- #
    # buffered objects


    # -------------------------------------------------- #

    def __init__(self):
        super().__init__(Template.TYPE, 0, 0)
        self.aregist = Template.ANIM_CATEGORY.create_registry_for_all()
        self.sprite = self.aregist[Template.IDLE_ANIM].get_frame()
        self.hitbox = self.aregist[Template.IDLE_ANIM].get_hitbox()
    
    def start(self):
        # whatever you want the entity to do before adding to world
        pass

    def update(self):
        # update function
        entityext.update_ani_and_hitbox(self, Template.IDLE_ANIM, handle=False)

        # lerp
        self.motion *= Template.LC

        # insert movement logic etc

        # update entity in world
        self.layer.world.move_entity(self)
        self.move_to_position()
    
    def render(self, surface):
        # render function
        surface.blit(self.sprite if self.motion.x < 0 else pygame.transform.flip(self.sprite, True, False), 
                self.get_glob_pos())

    def debug(self, surface):
        # debug function
        super().debug(surface)
        # any addition rendering you want

# -------------------------------------------------- #
# setup
EntityTypes.register_entity_type(Template.TYPE, Template)



