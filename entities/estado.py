from enum import Enum

class Estado(str, Enum):
    INICIAL = 'Inicial'
    CONFIGURACAO = 'Configuração'
    PARTIDA = 'Partida'