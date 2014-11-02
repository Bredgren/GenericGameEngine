
class GameObject(object):
    def __init__(self, gge):
        self.gge = gge
        self.__attributes = {}

    def setAttribute(self, AttributeType, value):
        """Sets the given attribute to the given value. Creates it if it
        doesn't exist."""
        if AttributeType in self.__attributes:
            attr = self.__attributes[AttributeType]
            attr.setValue(value)
        else:
            self.__attributes[AttributeType] = AttributeType(self, value)

    def getAttribute(self, AttributeType):
        return self.__attributes.get(AttributeType)

    def getAttributeValue(self, AttributeType):
        attribute = self.__attributes.get(AttributeType)
        if not attribute:
            return None
        return attribute.getValue()

    def getAttributes(self):
        return self.__attributes.copy()

    def delAttribute(self, AttributeType):
        """"""
        if AttributeType in self.__attributes:
            del self.__attributes[AttributeType]
