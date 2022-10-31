from fullsys import SysState

class Robot(object):

    def __init__(self):
        self._sys = SysState()

    def run(self):
        while True:
            self._sys.sysrun()

robot = Robot()
robot.run()