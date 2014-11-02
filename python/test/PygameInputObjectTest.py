
from gge.GenericGameEngine import GenericGameEngine
from gge.PygameInputObject import PygameInputObject
from gge.InputAttribute import InputAttribute

def testInit():
    print "Testing Initalization"

    gge = GenericGameEngine()
    py_obj = gge.newGameObject(PygameInputObject)

    assert py_obj.getAttributeValue(InputAttribute, "mouse pos") == (0, 0)
    assert py_obj.getAttributeValue(InputAttribute, "a") == False
    
def runTest():
    testInit()
    
if __name__ == "__main__":
    runTest()
