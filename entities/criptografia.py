from cryptography.fernet import Fernet
import base64, hashlib

class Criptografia:
    def __init__(self):
        self.chave = self.__getKey()
        self.fernetInstance = Fernet(self.chave)

    def __getKey(self):
        hlib = hashlib.md5()
        hlib.update(b'teste')
        return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))

    def criptografar(self, mensagem: bytes()):
        try:
            mensagemCriptografada = self.fernetInstance.encrypt(mensagem)
        except Exception as e:
            print(e)
            raise Exception("Erro na criptografia da palavra")
        return mensagemCriptografada

    def descriptografar(self, mensagem: bytes()):
        try:
            mensagemDescriptografada = self.fernetInstance.decrypt(mensagem)
        except Exception as e:
            print(e)
            raise Exception("Erro na descriptografia da palavra")
        return mensagemDescriptografada