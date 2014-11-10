
from gge.NullInputObject import NullInputObject
from gge.NullDisplayObject import NullDisplayObject

class GenericGameEngine(object):
    def __init__(self):
        self.__game_objects = set()
        self.__del_game_objects = set()
        self.__running = False
        self.__fps = 60
        self.__input_object = None
        self.__display_object = None

        self.setInputObjectType(NullInputObject)
        self.setDisplayObjectType(NullDisplayObject)

    def newGameObject(self, ObjectType):
        """Creates and returns a new GameObject of the given type."""
        obj = ObjectType(self)
        self.__game_objects.add(obj)
        return obj

    def delGameObject(self, object_instance):
        """Deletes the given GameObject instance if it exists."""
        for attribute in object_instance.getAttributes():
            object_instance.getAttribute(attribute).clearListeners()

        if self.__running:
            # Delete later
            self.__del_game_objects.add(object_instance)
        else:
            # Not running so we can delete now
            self.__game_objects.discard(object_instance)

    def getGameObjects(self):
        return frozenset(self.__game_objects)

    def setRunning(self, running):
        self.__running = running
        if running:
            self.__updateLoop()

    def getRunning(self):
        return self.__running

    def setFPS(self, fps):
        self.__fps = fps

    def getFPS(self):
        return self.__fps

    def setInputObjectType(self, InputObjectType):
        """The type of object that updates user input. Should be a subclass of
        GameObject and contain an InputAttribute attribute."""
        self.__input_object = InputObjectType(self)

    def getInputObject(self):
        return self.__input_object

    def setDisplayObjectType(self, DisplayObjectType):
        """The type of object that controls the display. Should be a subclass of
        GameObject."""
        self.__display_object = DisplayObjectType(self)

    def getDisplayObject(self):
        return self.__display_object

    def __updateLoop(self):
        while self.__running:
            self.__input_object.update(0)

            for obj in self.__game_objects:
                obj.update(0)

            # Must delete after iteration incase an object's update deletes
            # during iteration.
            self.__game_objects.difference_update(self.__del_game_objects)
            self.__del_game_objects.clear()

            self.__display_object.update(0)
