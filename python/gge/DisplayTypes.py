
from gge.Attribute import SingletonAttribute

class Layer(object):
    """
    name: "hud" | "foreground" | "background"
    number: #
    """
    __slots__ = ("name", "number")
    def __init__(self, name="foreground", number=0):
        self.name = "foreground"
        self.number = 0

    def __repr__(self):
        return "Layer(name=%r, number=%r)" % (self.name, self.number)

class DisplayRepType(object):
    """
    layer: Layer
    images: [Image, ..]
    shapes: [Shape, ..]
    """
    __slots__ = ("layer", "images", "shapes")
    def __init__(self, layer=Layer(), images=[], shapes=[]):
        self.layer = layer
        self.images = images
        self.shapes = shapes

class Offset(object):
    __slots__ = ("x", "y", "z")
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

class Image(object):
    """
    source: "/path/to/image.png"
    offset: Offset
    """
    __slots__ = ("source", "offset")
    def __init__(self, source="", offset=Offset()):
        self.source = source
        self.offset = offset

class Color(object):
    """
    r, g, b = 0 - 255
    """
    __slots__ = ("value")
    def __init__(self, color=(0, 0, 0)):
        self.value = color

    @property
    def r(self):
        return self.value[0]

    @r.setter
    def r(self, r):
        self.value = (r, self.value[1], self.value[2])

    @property
    def g(self):
        return self.value[1]

    @g.setter
    def g(self, g):
        self.value = (self.value[0], g, self.value[2])

    @property
    def b(self):
        return self.value[2]

    @b.setter
    def b(self, b):
        self.value = (self.value[0], self.value[1], b)

class ShapeColor(object):
    """
    line: Color
    fill: Color
    """
    __slots__ = ("line", "fill")
    def __init__(self, line=Color(), fill=Color()):
        self.line = line
        self.fill = fill

class Size(object):
    __slots__ = ("w", "h")
    def __init__(self, w=0, h=0):
        self.w = w
        self.h = h

class Shape(object):
    """
    type: "rectangle" | "oval" | "lines" | "polygon"
    # "rectangle" and "oval" are specified via "size"
    # "lines" and "polygon" are specified via "points"
    color: ShapeColor
    size: Size
    lineWidth: #
    points: [Point, ...]
    offset: Offset
    """
    __slots__ = ("type", "color", "size", "lineWidth", "points", "offset")
    def __init__(self, shape_type="rectangle", color=ShapeColor(),
                size=Size(), lineWidth=1,  points=[], offset=Offset()):
        self.type = shape_type
        self.color = color
        self.size = size
        self.lineWidth = lineWidth
        self.points = points
        self.offset = offset

class Point(object):
    __slots__ = ("x", "y", "z")
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

class Resolution(SingletonAttribute):
    """Value type is Size."""
    pass

class DisplayRep(SingletonAttribute):
    """Value type is DisplayRepType."""
    pass
