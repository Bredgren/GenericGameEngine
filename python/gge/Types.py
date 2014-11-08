
from gge.Attribute import SingletonAttribute

from collections import namedtuple

class Point(namedtuple("Point", "x y")):
    __slots__ = ()
    def __new__(_cls, x=0, y=0):
        return super(Point, _cls).__new__(_cls, x, y)

class Position(SingletonAttribute):
    """Value is Point."""
    pass
