
from gge.Attribute import SingletonAttribute

class DisplayRepType(object):
    """
    layer: Layer
    images: [Image, ..]
    shapes: [Shape, ..]
    text: [Text, ...]
    """
    __slots__ = ("layer", "images", "shapes", "text")
    def __init__(self, layer=None, images=[], shapes=[], text=[]):
        self.layer = layer if layer else Layer()
        self.images = images
        self.shapes = shapes
        self.text = text

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

class Image(object):
    """
    source: "/path/to/image.png"
    offset: Offset
    """
    __slots__ = ("source", "offset")
    def __init__(self, source="", offset=None):
        self.source = source
        self.offset = offset if offset else Offset()

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
    def __init__(self, shape_type="rectangle", color=None,
                size=None, lineWidth=1,  points=[], offset=None):
        self.type = shape_type
        self.color = color if color else ShapeColor()
        self.size = size if size else Size()
        self.lineWidth = lineWidth
        self.points = points
        self.offset = offset if offset else Offset()

class Text(object):
    __slots__ = ("text", "font", "size", "color", "offset")
    def __init__(self, text="", font="", size=10, color=None,
                 offset=None):
        self.text = text
        self.font = font
        self.size = size
        self.color = color if color else Color()
        self.offset = offset if offset else Offset()

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

class ShapeColor(object):
    """
    line: Color
    fill: Color
    """
    __slots__ = ("line", "fill")
    def __init__(self, line=None, fill=None):
        self.line = line if line else Color()
        self.fill = fill if fill else Color()

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

class Size(object):
    __slots__ = ("w", "h")
    def __init__(self, w=0, h=0):
        self.w = w
        self.h = h

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

class Resolution(SingletonAttribute):
    """Value type is Size."""
    pass

class Fullscreen(SingletonAttribute):
    """Value type is bool."""
    pass

class DisplayRep(SingletonAttribute):
    """Value type is DisplayRepType."""
    pass
