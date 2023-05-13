from cryptography.fernet import Fernet

class Criptografia:
    def __init__(self):
        self.chave = Fernet.generate_key()
        self.fernetInstance = Fernet(self.chave)

    def criptografar(self, mensagem: str):
        try:
            mensagemCriptografada = self.fernetInstance.encrypt(mensagem.encode())
        except Exception as e:
            raise Exception("Erro na criptografia da palavra")
        return mensagemCriptografada

    def descriptografar(self, mensagem: str):
        try:
            mensagemDescriptografada = self.fernetInstance.decrypt(mensagem).decode()
        except Exception as e:
            raise Exception("Erro na descriptografia da palavra")
        return mensagemDescriptografada