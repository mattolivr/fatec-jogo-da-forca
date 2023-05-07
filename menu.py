from enum import Enum

import forca
import index as operacoes
class Menu:
    class Opcoes(str, Enum):
        INI_CONFIGURAR = 'Configurar Jogo'
        INI_JOGAR = 'Iniciar Jogo'
        INI_ENCERRAR = 'Encerrar'
        
        CONF_ADICIONAR = 'Adicionar Palavra'
        CONF_REMOVER = 'Remover Palavra'
        CONF_ENCERRAR = 'Encerrar Configurações'
    
    def __init__(self, estadoForca: forca.Estado):
        self.listaOpcoes = self.getOpcoesMenu(estadoForca)
        self.montaMenu(estadoForca)

    def montaMenu(self, estadoForca: forca.Estado):
        self.listaOpcoes = self.getOpcoesMenu(estadoForca)

        contador = 0
        print ("== JOGO DA FORCA ==")
        for opcao in self.listaOpcoes:
            contador += 1
            print(str(contador) + " - " + opcao)

    def entraOpcao(self):
        entradaValida = False
        dado = 0

        entrada = input("Por favor, insira uma opção: ")
        while(not entradaValida):
            try:
                dado = int(entrada)
            except:
                entradaValida = False
            else:
                entradaValida = self.validaEntrada(dado)

            if (not entradaValida):
                print("Opção inexistente. Por favor, insira uma opção valida")
                entrada = input("")
        return dado
    
    def validaEntrada(self, dado: int):
        if (dado <= 0):
            return False
        
        if (dado > len(self.listaOpcoes)):
            return False
        return True

    def getOpcao(self, dado: int):
        return self.listaOpcoes[dado]
    
    def getOpcoesMenu(self, estadoForca: forca.Estado):
        match estadoForca:
            case forca.Estado.INICIAL:
                return [self.Opcoes.INI_JOGAR, 
                        self.Opcoes.INI_CONFIGURAR, 
                        self.Opcoes.INI_ENCERRAR]
            case forca.Estado.CONFIGURACAO:
                return [self.Opcoes.CONF_ADICIONAR, 
                        self.Opcoes.CONF_REMOVER, 
                        self.Opcoes.CONF_ENCERRAR]
        return []

    def getFuncaoOpcao(self, dado: int):
        match self.getOpcao(dado):
            case self.Opcoes.INI_CONFIGURAR:
                return operacoes.configurar
            case self.Opcoes.INI_JOGAR:
                return operacoes.jogar
            case self.Opcoes.INI_ENCERRAR:
                return operacoes.encerra
        # raise função não encontrada