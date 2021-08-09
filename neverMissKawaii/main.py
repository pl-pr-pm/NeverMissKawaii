import sys
sys.path.append('../')

from lib.speechRecognition.speech import speechRecognition
from lib.function.screenShot.screencapture import ScreenShot
from lib.util import _logger_setup
import logging
import config

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logging.basicConfig(level=logging.DEBUG)

class NeverMissKawaii():

    def main():
        FUNC_NAME = config.FUNC_NAME
        if FUNC_NAME == 'ScreenShot':
          sr = speechRecognition(ScreenShot)
          sr.run()

    if __name__ == "__main__":
        main()