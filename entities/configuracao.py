from .criptografia import Criptografia

class Configuracao:
    def __init__(self):
        self.__pathPalavras = 'palavras.txt'
        self.__palavras = []
        self.__palavras = self.getPalavras()
        self.criptografia = Criptografia()

    def adicionaPalavra(self, novaPalavra: str):
        if (novaPalavra != ''):
            if (not self.__existeNaLista(novaPalavra)):
                self.__palavras.append(novaPalavra.strip())
            else:
                raise ValueError("A palavra", palavra, "já existe na lista")

    def __existeNaLista(self, novaPalavra: str):
        for palavra in self.listaPalavras():
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
                print(self.__palavras.index(palavra) + 1, palavra, sep=' - ')
        else:
            print("Nenhuma palavra configurada")

    def salvaPalavras(self):
        print("Salvando configurações...")
        self.__salvaPalavrasArquivoConfig()

    def getPalavras(self) -> list[str]:
        if (len(self.__palavras) != 0):
            return self.__palavras
        else:
            return self.__getPalavrasArquivoConfig()

    def __salvaPalavrasArquivoConfig(self):
        palavras = self.__getMensagensEncriptografadas(self.__palavras)
        try:
            arquivo = open(self.__pathPalavras, 'w')
            arquivo.write(palavras)
        except Exception as e:
            print(e, '\n')
            raise Exception("Erro ao salvar. Por favor, tente novamente")
        finally:
            self.__palavras = []
            arquivo.close()

    def __getPalavrasArquivoConfig(self) -> list[str]:
        palavras = []
        try: 
            arquivo = open(self.__pathPalavras, 'r')
            palavras = arquivo.readlines()
            arquivo.close()
        except:
            palavras = []

        for indice, palavra in enumerate(palavras):
            palavras[indice] = palavra.replace('\n', '')

        return palavras

    def __getMensagensEncriptografadas(self, palavras: list[str]):
        dados = ''

        try:
            for palavra in palavras:
                dados += self.criptografia.criptografar(palavra).decode() + '\n'
        except Exception as e:
            print(e)
        else:
            return dados