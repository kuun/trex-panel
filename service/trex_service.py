from PyQt5.QtCore import QObject, pyqtSignal

from trex.astf.trex_astf_client import ASTFClient


class TrexService(QObject):
    connected = pyqtSignal()

    def __init__(self):
        super(TrexService, self).__init__()
        self.server = ''
        self.sync_port = 4501
        self.async_port = 4500
        self.client = None

    def connect(self, server, sync_port, async_port):
        self.server = server
        self.sync_port = sync_port
        self.async_port = async_port
        self.client = ASTFClient(server=self.server, sync_port=self.sync_port, async_port=self.async_port)
        self.client.connect()
        self.connected.emit()

    def close_client(self):
        if self.client is not None:
            if self.client.is_connected():
                self.client.disconnect()
            self.client = None

    def reconnect(self):
        self.disconnect()
        self.client = ASTFClient(server=self.server, sync_port=self.sync_port, async_port=self.async_port)
        self.connected.emit()

    def get_client(self) -> ASTFClient:
        return self.client

