
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
    text: [Text, ...]
    """
    __slots__ = ("layer", "images", "shapes", "text")
    def __init__(self, layer=Layer(), images=[], shapes=[], text=[]):
        self.layer = layer
        self.images = images
        self.shapes = shapes
        self.text = text

class Offset(object):
    __slots__ = ("value")
    def __init__(self, x=0, y=0, z=0):
        if isinstance(x, tuple):
            self.value = x
        else:
            self.value = (x, y, z)

    @property
    def x(self):
        return self.value[0]

    @x.setter
    def x(self, x):
        self.value = (x, self.value[1], self.value[2])

    @property
    def y(self):
        return self.value[1]

    @y.setter
    def y(self, y):
        self.value = (self.value[0], y, self.value[2])

    @property
    def z(self):
        return self.value[2]

    @z.setter
    def z(self, z):
        self.value = (self.value[0], self.value[1], z)

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
    def __init__(self, r=0, g=0, b=0):
        if isinstance(r, tuple):
            self.value = r
        else:
            self.value = (r, g, b)

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
    __slots__ = ("value")
    def __init__(self, x=0, y=0, z=0):
        if isinstance(x, tuple):
            self.value = x
        else:
            self.value = (x, y, z)

    @property
    def x(self):
        return self.value[0]

    @x.setter
    def x(self, x):
        self.value = (x, self.value[1], self.value[2])

    @property
    def y(self):
        return self.value[1]

    @y.setter
    def y(self, y):
        self.value = (self.value[0], y, self.value[2])

    @property
    def z(self):
        return self.value[2]

    @z.setter
    def z(self, z):
        self.value = (self.value[0], self.value[1], z)

class Text(object):
    __slots__ = ("text", "font", "size", "color", "offset")
    def __init__(self, text="", font="", size=10, color=Color(),
                 offset=Offset()):
        self.text = text
        self.font = font
        self.size = size
        self.color = color
        self.offset = offset

class Resolution(SingletonAttribute):
    """Value type is Size."""
    pass

class DisplayRep(SingletonAttribute):
    """Value type is DisplayRepType."""
    pass
