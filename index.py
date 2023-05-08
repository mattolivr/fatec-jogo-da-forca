from jogo import Jogo
from estado import Estado

jogo = Jogo()
jogo.setEstado(Estado.INICIAL)

while (True):
    if (jogo.exit):
        break
    
    jogo.mostraMenu()
    jogo.aguardaFuncao()