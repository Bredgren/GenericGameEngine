
from gge.Attribute import SingletonAttribute

class Resolution(SingletonAttribute):
    """A tuple of the form (width, height)."""
    pass

class DisplayRepresentation(SingletonAttribute):
    """A dictionary with the following structure. All fields are optional and the
    fields at the outer level may be specified multiple times. All position related
    fields are relative to the position of the GameObject this attribute is attached
    to.
    {
    "z": 0                      # Default: 0
    # Objects with a lower "z" are drawn first
    "image": {
        "offset": (x, y),            # Default: (0, 0)
        "src": "/path/to/image.png", # Default: "./image.png"
    },
    "shape": {
        "offset": (x, y),                        # Default: (0, 0)
        "color": (r, g, b)                       # Default: (0%, 0%, 0%)
        "type": "rectangle|oval|lines|polygon"   # Default: "rectangle"
        # "rectangle" and "oval" are specified via "size"
        # "lines" and "polygon" are specified via "points"
        "size": (w, h)                  # Default: (1, 1)
        "points": [(x, y), (x, y), ...] # Default: []
    },
    }"""
    pass
