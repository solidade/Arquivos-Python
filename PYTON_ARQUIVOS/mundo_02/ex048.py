# Cabeçalho
import time

print('\033[1:31m-=-\033[m' * 22)
print('\033[1:35mEXIBINDO NÚMEROS IMPARES MULTIPLOS DE 3 NO INTERVALO ENTRE 1 e 500\033[m')
print('\033[1:31m-=-\033[m' * 22)
# Estrutura de laço for + estrutura condicional if
s = 0
cont = 0
for c in range(1, 500):  # for c in range(1, 500, 2) isso tornaria o primeiro if desnecessário
    if c % 2 != 0:
        if c % 3 == 0:
            cont = cont + 1
            s = s + c
            print(c)
            time.sleep(0.1)
print("O somatório de todos os {} números acima é {}".format(cont, s))
