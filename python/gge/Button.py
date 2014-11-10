
from gge.GameObject import GameObject
from gge.InputAttribute import InputAttribute
from gge.Attribute import SingletonAttribute
import gge.Types as T
import gge.DisplayTypes as DT

class MouseWithin(SingletonAttribute): pass
class MouseDown(SingletonAttribute): pass

class ShapeButton(GameObject):
    def __init__(self, gge):
        super(ShapeButton, self).__init__(gge)

        self.__layer = DT.Layer("hud", 0)
        self.__shape = DT.Shape()
        self.__text = DT.Text()
        self.__display_info = DT.DisplayRepType(layer=self.__layer,
                                                shapes=[self.__shape],
                                                text=[self.__text])

        self.setAttribute(DT.DisplayRep, value=self.__display_info)
        self.setAttribute(MouseWithin, value=False)
        self.setAttribute(MouseDown, value=False)

        input_object = gge.getInputObject()
        input_attribute = input_object.getAttribute(InputAttribute)
        input_attribute.newListener(self.__inputListener)

    def setLayer(self, name, number):
        self.__layer.name = name
        self.__layer.number = number

    def setText(self, text):
        self.__text.text = text

    def setFont(self, font):
        self.__text.font = font

    def setFontSize(self, size):
        self.__text.size = size

    def setFontColor(self, color):
        self.__text.color = color

    def setTextOffset(self, offset):
        self.__text.offset = offset

    def setShapeType(self, shape):
        self.__shape.shape = shape

    def setFillColor(self, color):
        self.__shape.color.fill = color

    def setLineColor(self, color):
        self.__shape.color.line = color

    def setShapeSize(self, size):
        self.__shape.size = size

    def setLineWidth(self, width):
        self.__shape.lineWidth = width

    def setShapePoints(self, points):
        self.__shape.points = points

    def setShapeOffset(self, offset):
        self.__shape.offset = offset

    def __inputListener(self, key, value):
        if key == "mouse pos":
            pos = self.getAttributeValue(T.Position)
            size = self.__shape.size
            if (pos.x <= value[0] <= pos.x + size.w and
                pos.y <= value[1] <= pos.y + size.h):
                self.setAttribute(MouseWithin, value=True)
            else:
                self.setAttribute(MouseWithin, value=False)
        elif key == "mouse 1":
            if self.getAttributeValue(MouseWithin):
                if value:
                    self.setAttribute(MouseDown, value=True)
                else:
                    self.setAttribute(MouseDown, value=False)

class ImageButton(GameObject):
    pass
