import os

os.environ['TREX_EXT_LIBS'] = '../external_libs'

from trex.astf.trex_astf_client import ASTFClient


class TrexService:
    def __init__(self):
        self.server = ''
        self.sync_port = 4501
        self.async_port = 4500
        self.client = None

    def connect(self, server, sync_port, async_port):
        self.server = server
        self.sync_port = sync_port
        self.async_port = async_port
        self.disconnect()
        self.client = ASTFClient(server=self.server, sync_port=self.sync_port, async_port=self.async_port)

    def disconnect(self):
        if self.client is not None:
            if self.client.is_connected():
                self.client.disconnect()

    def reconnect(self):
        self.disconnect()
        self.client = ASTFClient(server=self.server, sync_port=self.sync_port, async_port=self.async_port)

    def get_clinet(self):
        return self.client

