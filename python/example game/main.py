
try:
    import gge
except ImportError:
    import sys
    sys.path.append("../")

from gge.GenericGameEngine import GenericGameEngine
from gge.PygameInputObject import PygameInputObject
from gge.PygameDisplayObject import PygameDisplayObject
from gge.DisplayTypes import Resolution
from gge.InputAttribute import InputAttribute

from ButtonObject.ButtonObject import ButtonObject

import pygame

class Main(object):
    def __init__(self):
        pygame.init()

        self.gge = GenericGameEngine()
        self.gge.setInputObjectType(PygameInputObject)
        self.gge.setDisplayObjectType(PygameDisplayObject)

        input_object = self.gge.getInputObject()
        input_attribute = input_object.getAttribute(InputAttribute)
        input_attribute.newListener(self.inputListener)

        display_object = self.gge.getDisplayObject()
        display_object.setAttribute(Resolution, value=(600, 400))

        button = self.gge.newGameObject(ButtonObject)

    def inputListener(self, key, value):
        if value and key in [ "quit", "escape" ]:
            print "Bye."
            self.gge.setRunning(False)

    def start(self):
        self.gge.setRunning(True)

        pygame.quit()

if __name__ == "__main__":
    main = Main()
    main.start()
