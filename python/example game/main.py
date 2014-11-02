
try:
    import gge
except ImportError:
    import sys
    sys.path.append("../")
     
from gge.GenericGameEngine import GenericGameEngine

class Main(object):
    def __init__(self):
        self.gge = GenericGameEngine()

    def start(self):
        self.gge.setRunning(True)

if __name__ == "__main__":
    main = Main()
    main.start()
