
from gge.Attribute import CollectionAttribute

class InputAttribute(CollectionAttribute):
    """A collection whose keys are buttons and values are True if the button is
    being pushed else False. Except for mouse_pos which always returns
    coordinates. Keys is case sensitive and symbols should be refered to by
    their non-shifted labels (e.g ',' not '<').

    Special buttons:
    'mouse pos', 'mouse 1', 'mouse 2', 'mouse 3'
    'f1' and other functions
    'num 1' and other numpad numbers
    'num /' and other numpad symbols including 'num enter' and 'numlock'
    'left ctrl', 'right ctrl'
    'left alt', 'right alt'
    'left shift', 'right shift'
    'escape', 'backspace', 'caps', 'enter', 'space', 'tab'
    'print screen', 'insert', 'delete', 'home', 'end', 'page up, 'page down'
    'left', 'right', 'up', 'down'
    'quit' - when the user quits via the window's X button
    """
    def __init__(self, owner):
        super(InputAttribute, self).__init__(owner)
