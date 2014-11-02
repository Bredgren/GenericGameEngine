
from gge.GameObject import GameObject
from gge.InputAttribute import InputAttribute

class NullInputObject(GameObject):
    def __init__(self, gge):
        super(NullInputObject, self).__init__(gge)
        self.setAttribute(InputAttribute)
        self.__attr = self.getAttribute(InputAttribute)
        self.__attr.setDefault(False)
        self.__attr.setValue('mouse pos', (0, 0))
        self.__given_warning = False

    def update(self, dt):
        if not self.__given_warning:
            print "Warning: Using the NULL input object"
            self.__given_warning = True
