def montaMenu(listaOpcoes):
    contador = 0
    print ("== JOGO DA FORCA ==")
    for opcao in listaOpcoes:
        contador += 1
        print(contador + " - " + opcao)

def entraOpcao():
    dado = int(input(""))
    return dado