import math

from configSetup import config

rankValido = config.getint('main', 'rankValido')
rankInvalido = config.getint('main', 'rankInvalido')

def applyRank(index, value):
    if(math.isnan(index)):
        return value * rankInvalido
    else:
        return value * rankValido
        
