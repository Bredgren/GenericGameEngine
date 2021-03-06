
class CollectionAttribute(object):
    """ """
    def __init__(self, owner):
        self.__owner = owner
        self.__listeners = set()
        self.__new_listeners = set()
        self.__del_listeners = set()
        self.__value = {}
        self.__default = None
        self.__notifying = False

    def newListener(self, function):
        """Calls the given function when the Attribute's value changes."""
        if self.__notifying:
            self.__new_listeners.add(function)
        else:
            self.__listeners.add(function)

    def delListener(self, function):
        """Deletes the given listener if it exists."""
        if self.__notifying:
            self.__del_listners.add(function)
        else:
            self.__listeners.add(function)

    def clearListeners(self):
        if self.__notifying:
            self.__del_listeners.update(self.__listeners)
        else:
            self.__listeners.clear()

    def getOwner(self):
        return self.__owner

    def getValue(self, key):
        """Returns the value associated with the given key or None if if it
        doesn't exist."""
        return self.__value.get(key, self.__default)

    def setValue(self, key, value):
        if value == self.__value.get(key):
            return
        self.__value[key] = value

        self.__notifying = True
        for listener in self.__listeners:
            listener(key, value)
        self.__notifying = False

        self.__listeners.update(self.__new_listeners)
        self.__new_listeners.clear()
        self.__listeners.difference_update(self.__del_listeners)
        self.__del_listeners.clear()

    def delValue(self, key):
        if key in self.__value:
            del self.__value[key]

    def setDefault(self, default):
        self.__default = default

    def getDefault(self):
        return self.__default

    def __contains__(self, key):
        return key in self.__value

class SingletonAttribute(object):
    """ """
    def __init__(self, owner, value=None):
        self.__owner = owner
        self.__listeners = set()
        self.__new_listeners = set()
        self.__del_listeners = set()
        self.__value = None
        self.setValue(value)
        self.__notifying = False

    def newListener(self, function):
        """Calls the given function when the Attribute's value changes."""
        if self.__notifying:
            self.__new_listners.add(function)
        else:
            self.__listeners.add(function)

    def delListener(self, function):
        """Deletes the given listener if it exists."""
        if self.__notifying:
            self.__del_listeners.add(function)
        else:
            self.__listeners.add(function)

    def clearListeners(self):
        if self.__notifying:
            self.__del_listeners.update(self.__listeners)
        else:
            self.__listeners.clear()

    def getOwner(self):
        return self.__owner

    def getValue(self):
        return self.__value

    def setValue(self, value):
        if value == self.__value:
            return
        self.__value = value

        self.__notifying = True
        for listener in self.__listeners:
            listener(value)
        self.__notifying = False

        self.__listeners.update(self.__new_listeners)
        self.__new_listeners.clear()
        self.__listeners.difference_update(self.__del_listeners)
        self.__del_listeners.clear()
