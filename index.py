from menu import Menu
from configuracao import Configuracao
from estado import Estado

class Jogo():

    def __init__(self):
        self.__setEstado(Estado.INICIAL)
        self.__menu = Menu(self.__getEstado())

    def configurar(self):
        config = Configuracao()

    def jogar(self):
        pass

    def encerrar(self):
        pass

    def mostraMenu(self):
        self.__menu.montaMenu(self.__getEstado())

    def aguardaDado(self):
        dado = self.__entraOpcao()
        self.__executaFuncao(dado)

    def __executaFuncao(self, dado: int):
        funcao = self.__getFuncaoOpcao(dado - 1)
        funcao(self)

    def __getFuncaoOpcao(self, dado: int):
        opcoes = self.__menu.Opcoes
        match self.__menu.getOpcao(dado):
            case opcoes.INI_CONFIGURAR:
                return Jogo.configurar
            case opcoes.INI_JOGAR:
                return Jogo.jogar
            case opcoes.INI_ENCERRAR:
                return Jogo.encerrar
        # raise função não encontrada

    def __entraOpcao(self):
        entradaValida = False
        dado = 0

        entrada = input("Por favor, insira uma opção: ")
        while(not entradaValida):
            try:
                dado = int(entrada)
            except:
                entradaValida = False
            else:
                entradaValida = self.__validaEntrada(dado)

            if (not entradaValida):
                print("Opção inexistente. Por favor, insira uma opção valida")
                entrada = input("")
        return dado

    def __validaEntrada(self, dado: int):
        if (dado <= 0):
            return False

        if (dado > len(self.__menu.listaOpcoes)):
            return False
        return True

    def __getEstado(self):
        return self.__estado
    
    def __setEstado(self, estado: Estado):
        self.__estado = estado

jogo = Jogo()

while (True):
    jogo.mostraMenu()
    jogo.aguardaDado()
