from enum import Enum
from forca import Estado

class Opcoes(str, Enum):
    INI_CONFIGURAR = 'Configurar Jogo'
    INI_JOGAR = 'Iniciar Jogo'
    INI_ENCERRAR = 'Encerrar'
    
    CONF_ADICIONAR = 'Adicionar Palavra'
    CONF_REMOVER = 'Remover Palavra'
    CONF_ENCERRAR = 'Encerrar Configurações'


def montaMenu(estadoForca: Estado):
    listaOpcoes = getOpcoesMenu(estadoForca)

    contador = 0
    print ("== JOGO DA FORCA ==")
    for opcao in listaOpcoes:
        contador += 1
        print(str(contador) + " - " + opcao)

def entraOpcao():
    dado = int(input(""))
    return dado

def getOpcoesMenu(estadoForca: Estado):
    match estadoForca:
        case Estado.INICIAL:
            return [Opcoes.INI_CONFIGURAR, Opcoes.INI_JOGAR, Opcoes.INI_ENCERRAR]
        case Estado.CONFIGURACAO:
            return [Opcoes.CONF_ADICIONAR, Opcoes.CONF_REMOVER, Opcoes.CONF_ENCERRAR]
    return []