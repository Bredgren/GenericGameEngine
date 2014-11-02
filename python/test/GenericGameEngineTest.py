
from gge.GenericGameEngine import GenericGameEngine
from gge.GameObject import GameObject

def testGameObject():
    print "Testing GameObject"
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

def testFPS():
    print "Testing FPS"
    gge = GenericGameEngine()
    
    gge.setFPS(30)
    assert gge.getFPS() == 30
    
    gge.setFPS(20)
    assert gge.getFPS() == 20

def testRunning():
    print "Testing Running"
    class Obj(GameObject):
        def __init__(self, gge):
            super(Obj, self).__init__(gge)
            self.count = 0
            
        def update(self, dt):
            self.count += 1
            if self.count >= 10:
                self.gge.delGameObject(self)
                # Shouldn't be actually deleted just yet
                objs = self.gge.getGameObjects()
                assert self in objs
                self.gge.setRunning(False)

    gge = GenericGameEngine()
    obj = gge.newGameObject(Obj)
    gge.setRunning(True)
    # Should be removed by the time setRunning returns
    objs = gge.getGameObjects()
    assert obj not in objs
    
def runTest():
    testGameObject()
    testFPS()
    testRunning()
    
if __name__ == "__main__":
    runTest()
