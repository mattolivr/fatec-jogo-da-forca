class Configuracao:
    def __init__(self):
        self.__pathArquivoConfig = 'config.txt'
        self.__palavras = []
        self.__palavras = self.getPalavras()

    def adicionaPalavra(self, novaPalavra: str):
        if (novaPalavra != ''):
            self.__palavras.append(str(novaPalavra))

    def removePalavra(self, palavra: str):
        try:
            self.__palavras.remove(palavra)
        except:
            raise ValueError("Palavra não existe na lista")

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
        print("== Palavras adicionadas ==")
        for palavra in palavras:
            # mostra o índice + 1 para ficar mais humano
            print(self.__palavras.index(palavra) + 1, palavra, sep=' - ', end='')

    def salvaPalavras(self):
        print("Salvando configurações...")
        self.__salvaPalavrasArquivoConfig()

    def getPalavras(self) -> list[str]:
        if (len(self.__palavras) != 0):
            return self.__palavras
        else:
            return self.__getPalavrasArquivoConfig()

    def __salvaPalavrasArquivoConfig(self):
        # TODO: implementar criptografia
        palavras = self.__retornaListaPalavrasSalvar(self.__palavras)
        try:
            arquivo = open(self.__pathArquivoConfig, 'w')
            arquivo.write(palavras)
        except Exception as e:
            print(e, '\n')
            raise Exception("Erro ao salvar. Por favor, tente novamente")
        finally:
            self.__palavras = []
            arquivo.close()

    def __retornaListaPalavrasSalvar(self, palavras: list[str]):
        novaLista = ''
        for palavra in palavras:
            novaLista += palavra + ' \n'
        return novaLista

    def __getPalavrasArquivoConfig(self) -> list[str]:
        try: 
            arquivo = open(self.__pathArquivoConfig, 'r')
            palavras = arquivo.readlines()
            arquivo.close()
            return palavras
        except:
            return []