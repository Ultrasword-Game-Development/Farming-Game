"""
plant.py
- for plants in the game
"""

from scripts import animationext, entityext


class Plant(entityext.NonGameEntity):
    """
    Plant

    - a plant in the game
    """

    NAME = "Plant"

    # -------------------------------------------------- #

    def __init__(self, name: str):
        super().__init__(Plant.NAME if not name else name, None)

    def update(self):
        pass

    def render(self):
        pass

