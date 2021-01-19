from abc import ABC


class EncryptionAlgorithm(ABC):
    def encrypt(self, message: str):
        pass


class AES(EncryptionAlgorithm):
    def encrypt(self, message: str):
        print('encrypting, using AES algorithm')
        return 'encrypted message'


class DES(EncryptionAlgorithm):
    def encrypt(self, message: str):
        print('encrypting, using DES algorithm')
        return 'encrypted message'


class ChatClient:
    def __init__(self, algorithm: EncryptionAlgorithm):
        self.algorithm = algorithm

    def send(self, message: str):
        self.algorithm.encrypt(message)


def driver():
    cc = ChatClient(AES())
    cc.send('hi AES')

    cc = ChatClient(DES())
    cc.send('hi DES')
