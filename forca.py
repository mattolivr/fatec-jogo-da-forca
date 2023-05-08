from enum import Enum
import random
class Forca:
    def __init__(self, palavras: list[str]):
        self.__palavra = self.__selecionaPalavra(palavras)
        self.layoutForca = self.__criaForca()

    def __criaForca(self):
        layout = [""] * 11
        layout[0] = "----------    "
        layout[1] = "|        |    "
        layout[2] = "|        O    "
        layout[3] = "|       /|\   "
        layout[4] = "|       / \   "
        layout[5] = "|             "
        layout[6] = "¯¯¯¯¯¯¯¯¯¯¯¯¯¯"

        layout[8] = "Palavra: " + ("_" * len(self.__palavra))
        layout[9] = "Acertos: "
        layout[10] = "Erros: "

        return layout        

    def __selecionaPalavra(self, palavras: list[str]):
        return random.choice(palavras)

    def adicionaErro(self):
        pass

    def adicionaAcerto(self):
        pass

    def verificaLetra(self):
        pass