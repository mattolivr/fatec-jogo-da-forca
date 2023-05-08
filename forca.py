from enum import Enum
import random
class Forca:
    def __init__(self, palavras: list[str]):
        self.__palavra = self.__selecionaPalavra(palavras)
        self.__acertos = []
        self.__erros = []
        self.layoutForca = self.__criaForca()

        self.__atualizaAcertos()
        self.__atualizaErros()

    def __criaForca(self):
        layout = [""] * 10
        layout[0] = "----------    "
        layout[1] = "|        |    "
        layout[2] = "|        O    "
        layout[3] = "|       /|\   "
        layout[4] = "|       / \   "
        layout[5] = "|             "
        layout[6] = "¯¯¯¯¯¯¯¯¯¯¯¯¯¯"

        return layout        

    def __selecionaPalavra(self, palavras: list[str]):
        return random.choice(palavras)

    def exibeForca(self):
        for linha in self.layoutForca:
            print(linha)

    def verificaLetra(self, letra: str) -> bool:
        if (letra in self.__palavra):
            return True
        return False

    def adicionaErro(self, letra: str):
        if (letra in self.__erros or letra in self.__acertos):
            raise Exception("Letra já inserida")

        self.__erros.append(letra)
        self.__atualizaErros()

    def __atualizaErros(self):
        erros = ""
        layout = self.layoutForca

        for erro in self.__erros:
            erros += erro + " ,"

        layout[9] = "Erros: " + erros

        match len(self.__erros):
            case 0:
                layout[2] = "|             "
                layout[3] = "|             "
                layout[4] = "|             "
            case 1:
                layout[2] = "|        O    "
            case 2:
                layout[3] = "|        |    "
            case 3:
                layout[3] = "|       /|    "
            case 4:
                layout[3] = "|       /|\   "
            case 5:
                layout[4] = "|       /     "
            case 6:
                layout[4] = "|       / \   "

    def adicionaAcerto(self, letra: str):
        if (letra in self.__erros or letra in self.__acertos):
            raise Exception("Letra já inserida")
        
        self.__acertos.append(letra)
        self.__atualizaAcertos()

    def __atualizaAcertos(self):
        acertos = ""

        for letra in self.__palavra:
            if (letra in self.__acertos):
                acertos += letra
            else:
                acertos += '_'
        self.layoutForca[8] = "Palavra: " + acertos

    def verificaLetra(self):
        pass