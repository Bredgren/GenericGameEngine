
class GameObject(object):
    def __init__(self, gge):
        self.gge = gge
        self.__attributes = {}

    def setAttribute(self, AttributeType, key=None, value=None):
        """Sets the given attribute to the given value. Creates it if it
        doesn't exist. Leave key=None to set singleton attributes"""
        if AttributeType in self.__attributes:
            attr = self.__attributes[AttributeType]
            if key != None:
                attr.setValue(key, value)
            elif value != None:
                attr.setValue(value)
        else:
            if key != None:
                self.__attributes[AttributeType] = AttributeType(self)
                self.__attributes[AttributeType].setValue(key, value)
            elif value != None:
                self.__attributes[AttributeType] = AttributeType(self, value)
            else:
                self.__attributes[AttributeType] = AttributeType(self)

    def getAttribute(self, AttributeType):
        return self.__attributes.get(AttributeType)

    def getAttributeValue(self, AttributeType, key=None):
        attribute = self.__attributes.get(AttributeType)
        if not attribute:
            return None
        if key != None:
            return attribute.getValue(key)
        return attribute.getValue()

    def getAttributes(self):
        return self.__attributes.copy()

    def delAttribute(self, AttributeType):
        """"""
        if AttributeType in self.__attributes:
            del self.__attributes[AttributeType]

    def update(self, dt):
        pass
