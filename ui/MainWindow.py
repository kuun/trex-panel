import sys

from PyQt5.QtWidgets import (QApplication, QPushButton,
                             QMessageBox, QHBoxLayout, QVBoxLayout, QGridLayout, QMainWindow, QMenu, QAction)

from ui.ConnectDialog import ConnectDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__init_ui()

    def __init_ui(self):
        self.create_menu()
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        grid = QGridLayout()
        names = ['Cls', 'Bck', '', 'Close', 
                 '7', '8', '9', '/', 
                 '4', '5', '6', '*',
                 '1', '2', '3', '-', 
                 '0', '.', '=', '+']
        positions = [(i, j) for i in range(5) for j in range(4)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        vbox = QVBoxLayout()
        vbox.addStretch(1)

        vbox.addLayout(grid)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)

        self.setMinimumSize(1000, 700)
        self.setWindowTitle('Window with button')
        self.show()

    def create_menu(self):
        menu_bar = self.menuBar()
        file_menu: QMenu = menu_bar.addMenu(self.tr('&File'))

        connect_act = QAction(self.tr('&Connect'), self)
        connect_act.setStatusTip(self.tr('Connect to TRex server'))
        connect_act.triggered.connect(self.open_connect_dialog)
        file_menu.addAction(connect_act)

    def open_connect_dialog(self):
        dlg = ConnectDialog(self)
        dlg.show()

    def closeEvent(self, ev):
        reply = QMessageBox.question(self, 'Message', 'Are you sure?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            ev.accept()
        else:
            ev.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()

    sys.exit(app.exec_())
