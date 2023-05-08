import os

from menu import Menu
from configuracao import Configuracao
from estado import Estado

class Jogo():

    def __init__(self):
        self.exit = False
        self.setEstado(Estado.INICIAL)
        self.__limpaConsole()
        self.__menu = Menu()

    def configurar(self):
        self.__configuracao = Configuracao()

        self.setEstado(Estado.CONFIGURACAO)
        self.mostraMenu()
        self.aguardaFuncao()

    def confAdicionaPalavra(self):
        palavra = input("Insira uma palavra: ")

        if (len(palavra) > 0):
            self.__configuracao.adicionaPalavra(palavra)
            print("Palavra", palavra, "adicionada")
            self.__confirmaFuncao()
        self.__limpaConsole()

    def confRemovePalavra(self):
        # TODO: adicionar remoção por índice
        self.__configuracao.listaPalavras()
        palavra = input("Insira uma palavra para remover: ")

        if (len(palavra) > 0):
            try:
                self.__configuracao.removePalavra(palavra)
            except Exception as e:
                print(str(e))
            else:
                print("Palavra", palavra, "removida")
            self.__confirmaFuncao()
        self.__limpaConsole()
        

    def confListaPalavras(self):
        self.__configuracao.listaPalavras()
        self.__confirmaFuncao()
        self.__limpaConsole()

    def confEncerrar(self):
        try:
            self.__configuracao.salvaPalavras()
        except Exception as e:
            print(e)
        else:
            print("Configurações salvas com sucesso")
            self.setEstado(Estado.INICIAL)

    def jogar(self):
        pass

    def encerrar(self):
        self.exit = True

    def mostraMenu(self):
        self.__menu.montaMenu(self.__getEstado())

    def aguardaFuncao(self):
        dado = self.__entraOpcao()
        self.__limpaConsole()
        self.__executaFuncao(dado)

    def __limpaConsole(self):
        if (os.name == 'Windows'):
            os.system('cls')
        else:
            os.system('clear')

    def __executaFuncao(self, dado: int):
        funcao = self.__getFuncaoOpcao(dado - 1)
        if (funcao != None):
            funcao()

    def __getFuncaoOpcao(self, dado: int):
        opcoes = self.__menu.Opcoes
        match self.__menu.getOpcao(dado):
            case opcoes.INI_CONFIGURAR:
                return self.configurar
            case opcoes.INI_JOGAR:
                return self.jogar
            case opcoes.INI_ENCERRAR:
                return self.encerrar
            case opcoes.CONF_ADICIONAR:
                return self.confAdicionaPalavra
            case opcoes.CONF_REMOVER:
                return self.confRemovePalavra
            case opcoes.CONF_LISTAR:
                return self.confListaPalavras
            case opcoes.CONF_ENCERRAR:
                return self.confEncerrar
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

    def __confirmaFuncao(self):
        input("Precione enter para continuar ")

    def __getEstado(self):
        return self.__estado
    
    def setEstado(self, estado: Estado):
        self.__estado = estado