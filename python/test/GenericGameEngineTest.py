
from gge.GenericGameEngine import GenericGameEngine
from gge.GameObject import GameObject

def runTest():
    gge = GenericGameEngine()
    objs = gge.getGameObjects()
    assert len(objs) == 0

    go1 = gge.newGameObject(GameObject)
    objs = gge.getGameObjects()
    assert go1 in gge.getGameObjects()
    assert len(objs) == 1
    
    go2 = gge.newGameObject(GameObject)
    objs = gge.getGameObjects()
    assert go1 in objs and go2 in objs
    assert len(objs) == 2

    gge.delGameObject(go1)
    objs = gge.getGameObjects()
    assert go1 not in objs and go2 in objs
    assert len(objs) == 1

    gge.delGameObject(go2)
    objs = gge.getGameObjects()
    assert len(objs) == 0
    
if __name__ == "__main__":
    runTest()
