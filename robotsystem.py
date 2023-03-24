from fullsys import SysState
from translate import Deepltranslate


class Robot(object):

    def __init__(self):
        self._sys = SysState()
        self._transjp = Deepltranslate()

    def run(self):
        text = "It's cold, isn't it? I heard that snow is falling in winter. In this season, there are snow festivals all over Japan. I looked it up, and it turns out that snow festivals are events where buildings and characters are created using snow. Have you ever been to a Snow Festival?"
        if text is not None and len(text) > 0:
            # self._sys.appendai()
            self._sys.question(text)
        while True:
            self._sys.sysrun()


robot = Robot()
robot.run()
