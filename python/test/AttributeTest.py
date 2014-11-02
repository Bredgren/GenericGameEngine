
from gge.Attribute import CollectionAttribute, SingletonAttribute

owner = None
listener_count = 0

def testCollectionAttribute():
    print "Testing CollectionAttribute"
    
    global listener_count
    listener_count = 0
    def listener(key, value):
        assert key == "a"
        global listener_count
        listener_count += 1
    
    c = CollectionAttribute(owner)
    c.newListener(listener)
    
    assert c.getOwner() == None
    assert c.getValue("a") == None
    assert "a" not in c
    
    c.setValue("a", 5)
    assert "a" in c
    assert c.getValue("a") == 5
    assert listener_count == 1
    
    c.delListener(listener)
    c.setValue("a", 4)
    assert "a" in c
    assert c.getValue("a") == 4
    assert listener_count == 1

    c.delValue("a")
    assert "a" not in c
    assert c.getValue("a") == None

def testSingletonAttribute():
    print "Testing SingletonAttribute"

    global listener_count
    listener_count = 0
    def listener(value):
        assert value == 10
        global listener_count
        listener_count += 1
        
    s = SingletonAttribute(owner, 0)
    s.newListener(listener)
    assert s.getOwner() == None
    assert s.getValue() == 0
    
    s.setValue(10)
    assert s.getValue() == 10
    assert listener_count == 1

    s.delListener(listener)
    s.setValue(11)
    assert s.getValue() == 11
    assert listener_count == 1
    
def runTest():    
    testCollectionAttribute()
    testSingletonAttribute()
    
if __name__ == "__main__":
    runTest()
