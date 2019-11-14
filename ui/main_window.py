from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QMessageBox, QMainWindow, QMenu, QAction,
                             QDockWidget, QTabWidget, QListWidget, QListWidgetItem)

from container import Container
from service.trex_service import TrexService
from trex.astf.trex_astf_client import ASTFClient
from ui.connect_dialog import ConnectDialog
from ui.system_info import SystemInfoPage


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.trex_service: TrexService = Container.trex_service()
        self.trex_service.connected.connect(self.handle_connected)
        self.__init_ui()

    def __init_ui(self):
        self.create_menu()

        self.port_list = QListWidget(self)
        dock = QDockWidget(self.tr('Port list'), self)
        dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        dock.setFeatures(QDockWidget.DockWidgetMovable)
        dock.setWidget(self.port_list)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)

        self.central_widget = QTabWidget(self)
        self.setCentralWidget(self.central_widget)

        self.setMinimumSize(1000, 700)
        self.setWindowTitle('TRex Panel')
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

    @pyqtSlot()
    def handle_connected(self):
        self.build_port_list()
        self.central_widget.clear()
        self.add_system_info_page()

    def add_system_info_page(self):
        system_info_page = SystemInfoPage(self)
        self.central_widget.addTab(system_info_page, self.tr('System info'))

    def build_port_list(self):
        client: ASTFClient = self.trex_service.get_client()
        info = client.get_server_system_info()
        ports = info.get('ports')
        font = QFont()
        font.setPointSize(14)
        for index, port in enumerate(ports, start=1):
            item = QListWidgetItem(self.port_list)
            item.setData(Qt.EditRole, port)
            item.setText(self.tr('Port ') + str(index))
            item.setFont(font)
