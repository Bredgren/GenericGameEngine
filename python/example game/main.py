
try:
    import gge
except ImportError:
    import sys
    sys.path.append("../")
     
from gge.GenericGameEngine import GenericGameEngine
from gge.PygameInputObject import PygameInputObject
from gge.InputAttribute import InputAttribute

import pygame

class Main(object):
    def __init__(self):
        pygame.init()
        display = pygame.display.set_mode((100, 100))
        
        self.gge = GenericGameEngine()
        self.gge.setInputObjectType(PygameInputObject)

        input_object = self.gge.getInputObject()
        input_attribute = input_object.getAttribute(InputAttribute)
        input_attribute.newListener(self.inputListener)

    def inputListener(self, key, value):
        if key == "quit" and value:
            print "Bye."
            self.gge.setRunning(False)

    def start(self):
        self.gge.setRunning(True)

        pygame.quit()

if __name__ == "__main__":
    main = Main()
    main.start()
