
from gge.GameObject import GameObject
from gge.InputAttribute import InputAttribute
from gge.Attribute import SingletonAttribute
import gge.Types as T
import gge.DisplayTypes as DT

class MouseWithin(SingletonAttribute): pass

class ButtonObject(GameObject):
    DEFAULT_COLOR = (255, 0, 0)
    HOVER_COLOR = (0, 0, 255)
    CLICK_COLOR = (0, 255, 0)

    def __init__(self, gge):
        super(ButtonObject, self).__init__(gge)

        self.__layer = DT.Layer("hud", 0)

        self.__color = DT.ShapeColor(fill=DT.Color(self.DEFAULT_COLOR))
        self.__size = DT.Size(w=100, h=50)
        self.__shape_rep = DT.Shape("rectangle", color=self.__color,
                                    size=self.__size, lineWidth=5)

        self.__display_info = DT.DisplayRepType(layer=self.__layer,
                                                shapes=[self.__shape_rep])

        self.setAttribute(DT.DisplayRep, value=self.__display_info)

        input_object = gge.getInputObject()
        input_attribute = input_object.getAttribute(InputAttribute)
        input_attribute.newListener(self.__inputListener)

        self.setAttribute(T.Position, value=T.Point(10, 10))

        self.setAttribute(MouseWithin, value=False)
        self.getAttribute(MouseWithin).newListener(self.__mouseWithinListener)

    def __inputListener(self, key, value):
        if key == "mouse pos":
            pos = self.getAttributeValue(T.Position)
            if (pos.x <= value[0] <= pos.x + self.__size.w and
                pos.y <= value[1] <= pos.y + self.__size.h):
                self.setAttribute(MouseWithin, value=True)
            else:
                self.setAttribute(MouseWithin, value=False)
        elif key == "mouse 1":
            if self.getAttributeValue(MouseWithin):
                if value:
                    self.__color.fill.value = self.CLICK_COLOR
                else:
                    self.__color.fill.value = self.HOVER_COLOR

    def __mouseWithinListener(self, value):
        if value:
            self.__color.fill.value = self.HOVER_COLOR
        else:
            self.__color.fill.value = self.DEFAULT_COLOR
