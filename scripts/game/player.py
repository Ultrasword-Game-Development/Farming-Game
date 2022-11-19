"""
player.py

- player object :)
"""
# -------------------------------------------------- #
# imports

import pygame

from engine.gamesystem.entity import EntityTypes
from engine.handler import filehandler, scenehandler
from engine.graphics import animation

from scripts import entityext, animationext

# -------------------------------------------------- #

animatino.load_and_parse_aseprite_animation("assets/sprites/player.json")


# -------------------------------------------------- #
# class

class Player(entityext.GameEntity):
    TYPE = "PLAYER"
    
    # -------------------------------------------------- #
    # animations
    ANIM_CAT = "player"
    IDLE_ANIM = "idle"

    # load
    ANIM_CATEGORY = animation.Category.get_category(ANIM_CAT)

    # -------------------------------------------------- #
    # statistics

    # -------------------------------------------------- #
    # signals

    # wrappers

    # -------------------------------------------------- #
    # buffered objects

    # -------------------------------------------------- #

    def __init__(self):
        super().__init__(Player.NAME, 0, 0)
        self.aregist = Player.ANIM_CATEGORY.create_registry_for_all()

        # set priority and camera
        self.camera = None
        self.priority = True
    
    def start(self):
        pass

    def update(self):
        pass

    def render(self, surface):
        pass

    def debug(self, surface):
        super().debug(surface)
    
    def kill(self):
        super().kill()

# -------------------------------------------------- #
# setup

EntityTypes.register_entity_type(Player.TYPE, Player)
