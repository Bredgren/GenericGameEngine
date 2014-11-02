
class GenericGameEngine(object):
    def __init__(self):
        self.__game_objects = set()

    def newGameObject(self, ObjectType):
        """Creates and returns a new GameObject of the given type."""
        obj = ObjectType(self)
        self.__game_objects.add(obj)
        return obj

    def delGameObject(self, object_instance):
        """Deletes the given GameObject instance if it exists."""
        self.__game_objects.discard(object_instance)

    def getGameObjects(self):
        return frozenset(self.__game_objects)

    
