
try:
    import gge
except ImportError:
    import sys
    sys.path.append("../")

from gge.GenericGameEngine import GenericGameEngine
from gge.PygameInputObject import PygameInputObject
from gge.InputAttribute import InputAttribute

import pygame

def runTest():
    pygame.init()

    display = pygame.display.set_mode((100, 100))
    
    gge = GenericGameEngine()
    py_obj = gge.newGameObject(PygameInputObject)

    running = True
    while running:
        py_obj.update(0)
        if py_obj.getAttributeValue(InputAttribute, 'quit'):
            running = False

    pygame.quit()
    
if __name__ == "__main__":
    print "Beginning interactive test"
    runTest()
