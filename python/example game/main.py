
try:
    import gge
except ImportError:
    import sys
    sys.path.append("../")

from gge.GenericGameEngine import GenericGameEngine
from gge.PygameInputObject import PygameInputObject
from gge.PygameDisplayObject import PygameDisplayObject
from gge.InputAttribute import InputAttribute
import gge.Types as T
import gge.DisplayTypes as DT

from gge.Button import ShapeButton, MouseWithin, MouseDown

import pygame

class Main(object):
    DEFAULT_COLOR = DT.Color(255, 50, 50)
    HOVER_COLOR = DT.Color(255, 150, 150)
    CLICK_COLOR = DT.Color(100, 0, 0)

    DEFAULT_FONT = "lucidasanstypewriterregular"
    HOVER_FONT = "lucidasanstypewriteroblique"
    CLICK_FONT = "lucidasanstypewriterregular"

    def __init__(self):
        pygame.init()

        self.gge = GenericGameEngine()
        self.gge.setInputObjectType(PygameInputObject)
        self.gge.setDisplayObjectType(PygameDisplayObject)

        input_object = self.gge.getInputObject()
        input_attribute = input_object.getAttribute(InputAttribute)
        input_attribute.newListener(self.__inputListener)

        display_object = self.gge.getDisplayObject()
        display_object.setAttribute(DT.Resolution, value=(600, 400))

        self.__current_buttons = set()

        self.__setupMainMenu()

    def start(self):
        self.gge.setRunning(True)
        pygame.quit()

    def stop(self):
        print "Bye."
        self.gge.setRunning(False)

    def __inputListener(self, key, value):
        if value and key in ["quit", "escape"]:
            self.stop()

    def __newButton(self):
        button = self.gge.newGameObject(ShapeButton)
        button.getAttribute(MouseWithin).newListener(self.__button1Within(button))
        button.getAttribute(MouseDown).newListener(self.__button1Down(button))

        button.setFillColor(self.DEFAULT_COLOR)

        button.setFont(self.DEFAULT_FONT)
        button.setFontSize(20)
        button.setTextOffset(DT.Offset(10, 10))

        self.__current_buttons.add(button)

        return button

    def __setupMainMenu(self):
        self.__cleanupMenu()

        def play(value):
            if not value:
                print "play"

        button = self.__newButton()
        button.setAttribute(T.Position, value=T.Point(50, 50))
        button.setText("Play")
        button.setShapeSize(DT.Size(115, 50))
        button.getAttribute(MouseDown).newListener(play)

        def settings(value):
            if not value:
                self.__setupSettingsMenu()

        button = self.__newButton()
        button.setAttribute(T.Position, value=T.Point(50, 125))
        button.setText("Settings")
        button.setShapeSize(DT.Size(115, 50))
        button.getAttribute(MouseDown).newListener(settings)

        def quit(value):
            if not value:
                self.stop()

        button = self.__newButton()
        button.setAttribute(T.Position, value=T.Point(50, 200))
        button.setText("Quit")
        button.setShapeSize(DT.Size(115, 50))
        button.getAttribute(MouseDown).newListener(quit)

    def __setupSettingsMenu(self):
        self.__cleanupMenu()

        def back(value):
            if not value:
                self.__setupMainMenu()

        button = self.__newButton()
        button.setAttribute(T.Position, value=T.Point(50, 50))
        button.setText("Back")
        button.setShapeSize(DT.Size(115, 50))
        button.getAttribute(MouseDown).newListener(back)

    def __cleanupMenu(self):
        for button in self.__current_buttons:
            self.gge.delGameObject(button)
        self.__current_buttons.clear()

    def __button1Within(self, button):
        def listener(value):
            if value:
                if button.getAttributeValue(MouseDown):
                    button.setFont(self.CLICK_FONT)
                    button.setFillColor(self.CLICK_COLOR)
                else:
                    button.setFont(self.HOVER_FONT)
                    button.setFillColor(self.HOVER_COLOR)
            else:
                button.setFont(self.DEFAULT_FONT)
                button.setFillColor(self.DEFAULT_COLOR)
        return listener

    def __button1Down(self, button):
        def listener(value):
            if value:
                button.setFont(self.CLICK_FONT)
                button.setFillColor(self.CLICK_COLOR)
            else:
                button.setFont(self.HOVER_FONT)
                button.setFillColor(self.HOVER_COLOR)
        return listener

if __name__ == "__main__":
    main = Main()
    main.start()
