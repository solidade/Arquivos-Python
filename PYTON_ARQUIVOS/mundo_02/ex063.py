# Variáveis com códigos de cores!
vermelho, amarelo, azul1, lilas, azul, fim = '\033[1:31m', '\033[1:33m', '\033[1:34m', '\033[1:35m', \
                                             '\033[1:36m', '\033[m'
# CONSTRUINDO UMA SEQUENCIA FIBONACCI
import time
from math import sqrt
# Cabeçalho
print('\033[1:31m-=-\033[m' * 11)
print('\033[1:35mEXIBINDO UMA SEQUENCIA FIBONACCI\033[m')
print('\033[1:31m-=-\033[m' * 11)
# Variáveis
n = int(input('Quantos termos da \033[33mSequência Fibonacci\033[m deseja exibir?: '))
tn = ((((1 + sqrt(5)) / 2) ** (n)) - (((1 - sqrt(5)) / 2) ** (n))) / sqrt(5)  #Formula fechada FIBONACCI
tnfix = tn  # GAMBIARRA NECESSÁRIA
nfix = 1  # GAMBIARRA NECESSÁRIA
while nfix <= n:
    tn = ((((1 + sqrt(5)) / 2) ** (nfix)) - (((1 - sqrt(5)) / 2) ** (nfix))) / sqrt(5)
    nfix = nfix + 1
    print('\033[36mO {}º termo é =\033[m \033[33m{:.0f}\033[m'.format(nfix - 1, tn))
