
from gge.GameObject import GameObject
from gge.Attribute import CollectionAttribute, SingletonAttribute

def testWithSingleton():
    class AttrSingle(SingletonAttribute):
        pass
    
    gge = None

    go = GameObject(gge)
    assert go.getAttribute(AttrSingle) == None
    assert go.getAttributeValue(AttrSingle) == None
    
    go.setAttribute(AttrSingle, value=1)
    assert go.getAttribute(AttrSingle).getValue() == 1
    assert go.getAttributeValue(AttrSingle) == 1
    
    go.setAttribute(AttrSingle, value=2)
    assert go.getAttribute(AttrSingle).getValue() == 2
    assert go.getAttributeValue(AttrSingle) == 2
    
    go.delAttribute(AttrSingle)
    assert go.getAttribute(AttrSingle) == None
    assert go.getAttributeValue(AttrSingle) == None

def testWithCollection():
    class AttrCol(CollectionAttribute):
        pass
    
    gge = None

    go = GameObject(gge)
    assert go.getAttribute(AttrCol) == None
    assert go.getAttributeValue(AttrCol) == None
    
    go.setAttribute(AttrCol, "a", 1)
    assert go.getAttribute(AttrCol).getValue("a") == 1
    assert go.getAttributeValue(AttrCol, "a") == 1

    go.setAttribute(AttrCol, "a", 2)
    assert go.getAttribute(AttrCol).getValue("a") == 2
    assert go.getAttributeValue(AttrCol, "a") == 2
    
    go.setAttribute(AttrCol, "b", 3)
    assert go.getAttribute(AttrCol).getValue("b") == 3
    assert go.getAttributeValue(AttrCol, "b") == 3
    
    go.delAttribute(AttrCol)
    assert go.getAttribute(AttrCol) == None
    assert go.getAttributeValue(AttrCol) == None
    
def runTest():
    testWithSingleton()
    testWithCollection()
    
if __name__ == "__main__":
    runTest()
