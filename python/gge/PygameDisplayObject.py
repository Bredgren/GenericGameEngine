
from gge.GameObject import GameObject
from gge.DisplayTypes import Resolution

import pygame

from collections import defaultdict

class PygameDisplayObject(GameObject):
    """Assumes pygame is initialized.
    Attributes:
       Resolution"""
    def __init__(self, gge):
        super(PygameDisplayObject, self).__init__(gge)

        self.setAttribute(Resolution)
        res = self.getAttribute(Resolution)
        res.newListener(self.__handleResolution)
        self.setAttribute(Resolution, value=(100, 100))

    def update(self, dt):
        reps = defaultdict(set)
        for game_object in self.gge.getGameObjects():
            rep = game_object.getAttributeValue(DisplayAttribute)
            if not rep:
                continue
            reps[rep["z"]].add(rep)

        for z in sorted(reps.keys()):
            for rep in reps[z]:
                self.__drawReperesentation(rep)

    def __drawRepresentation(self, rep):
        pass

    def __handleResolution(self, value):
        self.__display = pygame.display.set_mode(value)
