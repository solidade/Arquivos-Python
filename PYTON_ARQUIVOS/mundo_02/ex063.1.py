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
t1 = 0
t2 = 1
cont = 3
print('{} -> {}'.format(t1, t2), end='')
while cont <= n + 1:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont = cont + 1
    print(' -> {}'.format(t3), end='')
print(' -> FIM')