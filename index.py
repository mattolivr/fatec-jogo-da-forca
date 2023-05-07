from menu import Menu
from forca import Estado

# CONFIGURAÇÃO
def configurar():
    pass

def iniciaConfiguracao():
    pass

def encerraConfiguracao():
    pass

# PARTIDA
def jogar():
    pass

def iniciaPartida():
    pass

def encerraPartida():
    pass

# ENCERRA APLICAÇÃO
def encerra():
    pass

menu = Menu(Estado.INICIAL)
func = menu.getFuncaoOpcao(menu.entraOpcao())
func()