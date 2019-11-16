from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox

from container import Container
from service.trex_service import TrexService


class SystemInfoPage(QWidget):
    def __init__(self, parent):
        super(SystemInfoPage, self).__init__(parent)
        self.trex_service: TrexService = Container.trex_service()
        self.__init_ui()

    def __init_ui(self):
        client = self.trex_service.get_client()
        if client is None:
            return

        info = client.get_server_system_info()
        version = client.get_server_version()

        groupBox = QGroupBox('TRex server information', self)

        form = QFormLayout()
        form.addRow(self.tr('<b>Server:'), QLabel(self.trex_service.server))
        form.addRow(self.tr('<b>Sync port:'), QLabel(str(self.trex_service.sync_port)))
        form.addRow(self.tr('<b>Async port:'), QLabel(str(self.trex_service.async_port)))
        form.addRow(self.tr('<b>Version:'), QLabel(version['version'] + ' @ ' + version['mode']))
        form.addRow(self.tr('<b>CPU:</b>'), QLabel(info.get('core_type')))
        form.addRow(self.tr('<b>Port count:</b>'), QLabel(str(info.get('port_count'))))
        form.addRow(self.tr('<b>Up time:</b>'), QLabel(info.get('uptime')))

        groupBox.setLayout(form)

        vbox = QVBoxLayout()
        vbox.addWidget(groupBox)
        vbox.addStretch(1)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addStretch(1)
        self.setLayout(hbox)