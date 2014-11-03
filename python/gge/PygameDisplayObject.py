
from gge.GameObject import GameObject

import pygame

class PygameDisplayObject(GameObject):
    """Assumes pygame is initialized."""
    def __init__(self, gge):
        super(PygameDisplayObject, self).__init__(gge)
        self.__display = pygame.display.set_mode((500, 500))

    # def setResolution(self, resolution):
    #     pass

    # def setFullScreen(self, fullscreen):
    #     pass

    def update(self, dt):
        for game_object in self.gge.getGameObjects():
            rep = game_object.getDisplayRepresentation()
            if not rep:
                continue
            self.__drawReperesentation(rep)

    def __drawRepresentation(self, rep):
        pass
