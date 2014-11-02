
from gge.GameObject import GameObject
from gge.Attribute import CollectionAttribute, SingletonAttribute

def runTest():
    class AttrSingle(SingletonAttribute):
        pass
    
    gge = None

    go = GameObject(gge)
    assert go.getAttribute(AttrSingle) == None
    assert go.getAttributeValue(AttrSingle) == None
    
    go.setAttribute(AttrSingle, 1)
    assert go.getAttribute(AttrSingle).getValue() == 1
    assert go.getAttributeValue(AttrSingle) == 1
    
    go.setAttribute(AttrSingle, 2)
    assert go.getAttribute(AttrSingle).getValue() == 2
    assert go.getAttributeValue(AttrSingle) == 2
    
    go.delAttribute(AttrSingle)
    assert go.getAttribute(AttrSingle) == None
    assert go.getAttributeValue(AttrSingle) == None
    
if __name__ == "__main__":
    runTest()
