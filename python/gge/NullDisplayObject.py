
from gge.GameObject import GameObject

class NullDisplayObject(GameObject):
    def __init__(self, gge):
        super(NullDisplayObject, self).__init__(gge)
    #     self.setAttribute(InputAttribute)
    #     self.__attr = self.getAttribute(InputAttribute)
    #     self.__attr.setDefault(False)
    #     self.__attr.setValue('mouse pos', (0, 0))
        self.__given_warning = False

    def update(self, dt):
        if not self.__given_warning:
            print "Warning: Using the NULL display object"
            self.__given_warning = True
