# inicia_jogo
# encerra_jogo
# inicia_configuracao
# encerra_jogo

from menu import Menu
from forca import Estado

menu = Menu()
menu.montaMenu(Estado.INICIAL)
func = menu.getFuncaoOpcao(menu.entraOpcao())
func()