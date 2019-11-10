from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QHBoxLayout, QVBoxLayout, QFormLayout, QLineEdit, QSpinBox


class ConnectDialog(QDialog):
    def __init__(self, parent=None):
        super(ConnectDialog, self).__init__(parent)
        self.__init_ui()

    def __init_ui(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        # build form
        form = QFormLayout()
        vbox.addLayout(form)
        ip_edit = QLineEdit(self)
        form.addRow(self.tr('TRex IP:'), ip_edit)
        rpc_port_edit = QSpinBox()
        rpc_port_edit.setRange(1, 65535)
        rpc_port_edit.setValue(4501)
        form.addRow(self.tr('RPC Port:'), rpc_port_edit)
        zmq_port_edit = QSpinBox()
        zmq_port_edit.setRange(1, 65535)
        zmq_port_edit.setValue(4500)
        form.addRow(self.tr('ZMQ Port:'), zmq_port_edit)
        scapy_port_edit = QSpinBox()
        scapy_port_edit.setRange(1, 65535)
        scapy_port_edit.setValue(4507)
        form.addRow(self.tr('Scapy Port'), scapy_port_edit)

        hbox = QHBoxLayout()
        vbox.addLayout(hbox)

        hbox.addStretch(1)
        connectBtn = QPushButton(self.tr('Connect'), self)
        hbox.addWidget(connectBtn)
        cancelBtn = QPushButton(self.tr('Cancel'), self)
        cancelBtn.clicked.connect(self.cancel)
        hbox.addWidget(cancelBtn)

        self.setWindowTitle(self.tr('Connect to TRex'))
        self.setWindowModality(Qt.ApplicationModal)
        self.setModal(True)

    def cancel(self):
        self.close()

    def connect_server(self):
        pass