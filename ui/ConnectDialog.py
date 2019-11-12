import traceback

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QHBoxLayout, QVBoxLayout, QFormLayout, QLineEdit, QSpinBox, \
    QMessageBox

from trex.astf.trex_astf_client import ASTFClient


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
        self.ip_edit = QLineEdit(self)
        form.addRow(self.tr('TRex IP:'), self.ip_edit)
        self.rpc_port_edit = QSpinBox()
        self.rpc_port_edit.setRange(1, 65535)
        self.rpc_port_edit.setValue(4501)
        form.addRow(self.tr('RPC Port:'), self.rpc_port_edit)
        self.zmq_port_edit = QSpinBox()
        self.zmq_port_edit.setRange(1, 65535)
        self.zmq_port_edit.setValue(4500)
        form.addRow(self.tr('ZMQ Port:'), self.zmq_port_edit)
        self.scapy_port_edit = QSpinBox()
        self.scapy_port_edit.setRange(1, 65535)
        self.scapy_port_edit.setValue(4507)
        form.addRow(self.tr('Scapy Port'), self.scapy_port_edit)

        hbox = QHBoxLayout()
        vbox.addLayout(hbox)

        hbox.addStretch(1)
        connect_btn = QPushButton(self.tr('Connect'), self)
        connect_btn.clicked.connect(self.connect_server)
        hbox.addWidget(connect_btn)
        cancel_btn = QPushButton(self.tr('Cancel'), self)
        cancel_btn.clicked.connect(self.cancel)
        hbox.addWidget(cancel_btn)

        self.setWindowTitle(self.tr('Connect to TRex'))
        self.setWindowModality(Qt.ApplicationModal)
        self.setModal(True)

    def cancel(self):
        self.close()

    def connect_server(self):
        server = self.ip_edit.text()
        rpc_port = self.rpc_port_edit.value()
        zmq_port = self.zmq_port_edit.value()
        client = ASTFClient(server=server, sync_port=rpc_port, async_port=zmq_port)
        try:
            client.connect()
            msg_box = QMessageBox()
            msg_box.setText('Successfuly')
            msg_box.exec()
        except Exception as e:
            print('failed to connect to TRex server:', traceback.format_exc())
            msg_box = QMessageBox()
            msg_box.setText('Failed')
            msg_box.exec()