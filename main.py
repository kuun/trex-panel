import sys
import os

os.environ['TREX_EXT_LIBS'] = './external_libs'

from PyQt5.QtWidgets import QApplication

from ui.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()

    sys.exit(app.exec_())