
from PyQt5.QtWidgets import QApplication
from lib.app.sensors.udp_detector import UDPDetector
from lib.app.gui.controllers.screencontroller import ScreenController
import sys

if __name__ == "__main__":
    try:
        UDPDetector(8080).start()
        app = QApplication(sys.argv)
        screen_controller: ScreenController = ScreenController()
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        app.exit()

