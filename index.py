from menu import Menu
from configuracao import Configuracao
from estado import Estado

class Jogo():

    def __init__(self):
        self.setEstado(Estado.INICIAL)
        self.__menu = Menu()

    def configurar(self):
        self.__configuracao = Configuracao()

        self.setEstado(Estado.CONFIGURACAO)
        self.mostraMenu()
        self.aguardaFuncao()

    def confAdicionaPalavra(self):
        palavra = input("Insira uma palavra: ")

        if (len(palavra) > 0):
            self.__configuracao.adicionaPalavra(self)

        print("palavra", palavra, "adicionada")

    def confRemovePalavra(self):
        # TODO: adicionar remoção por índice
        palavra = input("Insira uma palavra: ")

        try:
            self.__configuracao.removePalavra(palavra)
        except e:
            print(str(e))

    def confListaPalavras(self):
        self.__configuracao.listaPalavras()

    def confEncerrar():
        jogo.setEstado(Estado.INICIAL)

    def jogar(self):
        pass

    def encerrar(self):
        pass

    def mostraMenu(self):
        self.__menu.montaMenu(self.__getEstado())

    def aguardaFuncao(self):
        dado = self.__entraOpcao()
        self.__executaFuncao(dado)

    def __executaFuncao(self, dado: int):
        funcao = self.__getFuncaoOpcao(dado - 1)
        if (funcao != None):
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
            case opcoes.CONF_ADICIONAR:
                return Jogo.confAdicionaPalavra
            case opcoes.CONF_REMOVER:
                return Jogo.confRemovePalavra
            case opcoes.CONF_LISTAR:
                return Jogo.confListaPalavras
            case opcoes.CONF_ENCERRAR:
                return Jogo.confEncerrar
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
    
    def setEstado(self, estado: Estado):
        self.__estado = estado

jogo = Jogo()
jogo.setEstado(Estado.INICIAL)

while (True):
    jogo.mostraMenu()
    jogo.aguardaFuncao()
