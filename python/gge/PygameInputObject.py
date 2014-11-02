
from gge.GameObject import GameObject
from gge.InputAttribute import InputAttribute

import pygame
from pygame.locals import *

class PygameInputObject(GameObject):
    """Assumes pygame is initialized."""
    def __init__(self, gge):
        super(PygameInputObject, self).__init__(gge)
        self.setAttribute(InputAttribute)
        self.__attr = self.getAttribute(InputAttribute)
        self.__attr.setDefault(False)
        self.__attr.setValue('mouse pos', (0, 0))

    def update(self, dt):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.__attr.setValue("quit", True)
            elif event.type == KEYDOWN:
                button = self.__getButtonName(event.key)
                if button:
                    self.__attr.setValue(button, True)
            elif event.type == KEYUP:
                button = self.__getButtonName(event.key)
                if button:
                    self.__attr.setValue(button, False)
            elif event.type == MOUSEMOTION:
                self.__attr.setValue("mouse pos", event.pos)
            elif event.type == MOUSEBUTTONDOWN:
                button = "mouse {}".format(event.button)
                self.__attr.setValue(button, True)
            elif event.type == MOUSEBUTTONUP:
                button = "mouse {}".format(event.button)
                self.__attr.setValue(button, False)

    def __getButtonName(self, pygame_key):
        name = pygame.key.name(pygame_key)
        if "[" in name and "]" in name:
            name = "num {}".format(name[1:-1])
        elif pygame_key == K_KP_ENTER:
            name = "num enter"
        elif pygame_key == K_RETURN:
            name = "enter"
        return name
