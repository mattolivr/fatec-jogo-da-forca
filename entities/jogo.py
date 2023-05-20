import os

from .menu import Menu
from .configuracao import Configuracao
from .estado import Estado
from .forca import Forca

class Jogo():
    def __init__(self):
        self.exit = False
        self.ESC = '\x1b'
        self.setEstado(Estado.INICIAL)
        self.__limpaConsole()
        self.__menu = Menu()
        self.__configuracao = Configuracao()

    def configurar(self):
        self.setEstado(Estado.CONFIGURACAO)
        self.mostraMenu()
        self.aguardaFuncao()

    def __confAdicionaPalavra(self):
        palavra = input("Insira uma palavra: ")

        if (len(palavra) > 0):
            try:
                self.__configuracao.adicionaPalavra(palavra)
            except Exception as e:
                print(e)
            else:
                print("Palavra", palavra, "adicionada")
            finally:
                self.__mostraConfirmacao()
        self.__limpaConsole()

    def __confRemovePalavra(self):
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
            self.__mostraConfirmacao()
        self.__limpaConsole()
        

    def __confListaPalavras(self):
        self.__configuracao.listaPalavras()
        self.__mostraConfirmacao()
        self.__limpaConsole()

    def __confEncerrar(self):
        try:
            self.__configuracao.salvaPalavras()
        except Exception as e:
            print(e)
        else:
            print("Configurações salvas com sucesso")
            self.setEstado(Estado.INICIAL)

    def jogar(self):
        try:
            self.__partidaIniciar()
        except Exception as exception:
            print(exception)
            return
        
        while(True):
            self.__limpaConsole()
            self.__forca.exibeForca()
            
            try:
                letra = self.__partidaEntraLetra()

                if (letra == self.ESC):
                    if (self.__mostraEscolhaBooleana("Deseja encerrar o jogo?")):
                        break

                if (self.__forca.verificaLetra(letra)):
                    self.__forca.adicionaAcerto(letra)
                else:
                    if (letra != self.ESC):
                        self.__forca.adicionaErro(letra)
            except Exception as exception:
                print(exception)
                self.__mostraConfirmacao()
            else:
                if (self.__validaEncerramento()):
                    self.__mostraConfirmacao()
                    break
        
        self.setEstado(Estado.INICIAL)
        self.__limpaConsole()
        
    def __partidaIniciar(self):
        palavrasConfiguradas = self.__configuracao.getPalavras()
        if (len(palavrasConfiguradas) == 0):
            raise Exception("Nenhuma palavra encontrada. Por favor, realize a configuração")

        self.setEstado(Estado.PARTIDA)
        self.__forca = Forca(palavrasConfiguradas)

    def __partidaEntraLetra(self):
        letra = str(input("Digite uma letra: "))

        if(len(letra) != 1):
            raise Exception("Insira apenas uma letra!") 

        if(letra.isnumeric()):
            raise Exception("São aceitas somente letras!")

        return letra

    def __validaEncerramento(self):
        self.__limpaConsole()
        self.__forca.exibeForca()

        if (self.__forca.validaVitoria()):
            print("=== VOCÊ VENCEU! ===")
            return True
        if (self.__forca.validaDerrota()):
            # TODO: confirmação "quer tentar novamente?"
            print("=== FIM DE JOGO ===")
            print("Você perdeu. Mas não desista, tente de novo!")
            print("A palavra era:", self.__forca.palavra)
            return True
        return False
    
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

    def __mostraEscolhaBooleana(self, msg: str):
        print(msg, "Enter para sim, Esc para não")
        entrada = None

        while(entrada != self.ESC or entrada != ''):
            entrada = input("")

            if (entrada == self.ESC):
                return False
            if (entrada == ''):
                return True

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
                return self.__confAdicionaPalavra
            case opcoes.CONF_REMOVER:
                return self.__confRemovePalavra
            case opcoes.CONF_LISTAR:
                return self.__confListaPalavras
            case opcoes.CONF_ENCERRAR:
                return self.__confEncerrar
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

    def __mostraConfirmacao(self):
        input("Precione enter para continuar ")

    def __getEstado(self):
        return self.__estado
    
    def setEstado(self, estado: Estado):
        self.__estado = estado