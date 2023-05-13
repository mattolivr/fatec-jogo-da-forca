from enum import Enum
from .estado import Estado

class Menu:
    class Opcoes(str, Enum):
        INI_CONFIGURAR = 'Configurar Jogo'
        INI_JOGAR = 'Iniciar Jogo'
        INI_ENCERRAR = 'Encerrar'

        CONF_ADICIONAR = 'Adicionar Palavra'
        CONF_REMOVER = 'Remover Palavra'
        CONF_LISTAR = 'Listar Palavras'
        CONF_ENCERRAR = 'Encerrar Configurações'

    def montaMenu(self, estadoForca: Estado):
        self.listaOpcoes = self.getOpcoesMenu(estadoForca)

        contador = 0
        print("== JOGO DA FORCA ==")
        for opcao in self.listaOpcoes:
            contador += 1
            print(str(contador) + " - " + opcao)

    def getOpcao(self, dado: int):
        return self.listaOpcoes[dado]

    def getOpcoesMenu(self, estadoForca: Estado):
        match estadoForca:
            case Estado.INICIAL:
                return [self.Opcoes.INI_JOGAR,
                        self.Opcoes.INI_CONFIGURAR,
                        self.Opcoes.INI_ENCERRAR]
            case Estado.CONFIGURACAO:
                return [self.Opcoes.CONF_ADICIONAR,
                        self.Opcoes.CONF_REMOVER,
                        self.Opcoes.CONF_LISTAR,
                        self.Opcoes.CONF_ENCERRAR]
        return []
