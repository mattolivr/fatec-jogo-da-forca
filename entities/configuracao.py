import os
from .criptografia import Criptografia

class Configuracao:
    def __init__(self):
        self.__pathPalavras = 'palavras.txt'
        self.criptografia = Criptografia()
        self.__palavras = self.__getPalavrasArquivoConfig()

    def adicionaPalavra(self, novaPalavra: str):
        if (novaPalavra != ''):

            for letra in novaPalavra:
                if(letra.isnumeric()):
                    raise Exception("São aceitas somente letras!")
            
            if (not self.__existeNaLista(novaPalavra)):
                self.__palavras.append(novaPalavra.strip())
            else:
                raise ValueError("A palavra", novaPalavra, "já existe na lista")

    def __existeNaLista(self, novaPalavra: str):
        lista = self.getPalavras()
        for palavra in lista:
            if (palavra.lower() == novaPalavra.lower()):
                return True
        return False

    def removePalavra(self, palavra: str):
        try:
            self.__palavras.remove(palavra)
        except:
            raise ValueError("A palavra inserida não existe na lista")

    def removePalavraIndice(self, indicePalavra: int):
        # trata entrada humana como começando em 1, então subtrai para corrigir
        indicePalavra =- 1
        if (indicePalavra <= 0):
            raise ValueError("Opção inexistente. Por favor, insira um valor válido")
        
        try:
            self.__palavras.pop(indicePalavra)
        except IndexError:
            raise ValueError("Palavra não existe na lista")

    def listaPalavras(self):
        palavras = self.getPalavras()
        if (len(palavras) > 0):
            print("== Palavras adicionadas ==")
            for palavra in palavras:
                # mostra o índice + 1 para ficar mais humano
                if (self.__existeNaLista(palavra)):
                    print(palavras.index(palavra) + 1, palavra, sep=' - ')
        else:
            print("Nenhuma palavra configurada")

    def salvaPalavras(self):
        print("Salvando configurações...")
        self.__salvaPalavrasArquivoConfig()

    def getPalavras(self) -> list[str]:
        if (len(self.__palavras) != 0):
            listaPalavras = self.__palavras
        else:
            listaPalavras = self.__getPalavrasArquivoConfig()

        return listaPalavras

    def __salvaPalavrasArquivoConfig(self):
        palavras = self.__getMensagensEncriptografadas(self.__palavras)
        try:
            arquivo = open(self.__pathPalavras, 'wb')
            
            for palavra in palavras:
                arquivo.write(palavra + b'\n')
        except Exception as e:
            print(e, '\n')
            raise Exception("Erro ao salvar. Por favor, tente novamente")
        finally:
            arquivo.close()

    def __getPalavrasArquivoConfig(self) -> list[bytes()]:
        palavras = []
        try: 
            arquivo = open(self.__pathPalavras, 'rb')
            palavrasLidas = arquivo.readlines()

            for palavra in palavrasLidas:
                palavras.append(self.criptografia.descriptografar(palavra).decode())
        except FileNotFoundError:
            arquivo = open(self.__pathPalavras, 'w')
        except Exception as e:
            print(e)
            palavras = []
        else:
            self.__palavras = palavras
        finally:
            arquivo.close()
        return palavras

    def __getMensagensEncriptografadas(self, palavras: list[str]):
        dados = []
        try:
            for palavra in palavras:
                dados.append(self.criptografia.criptografar(palavra.encode()))
        except Exception as e:
            print(e)
        else:
            return dados