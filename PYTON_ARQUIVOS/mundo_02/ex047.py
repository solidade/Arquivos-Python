# IMPRIMINDO OS NUMEROS PARES ENTRE 0 e 50
import time
# Cabeçalho
print('\033[1:31m-=-\033[m' * 16)
print('\033[1:35mEXIBINDO NÚMEROS PARES NO INTERVALO ENTRE 1 e 50\033[m')
print('\033[1:31m-=-\033[m' * 16)
# Estrutura de laço for + estrutura condicional if
for c in range(1, 50):
    if c % 2 == 0:
        print(c)
        time.sleep(0.1)
print("Finish!")
# OUTRA POSSIBILIDADE: for c in range (2, 50, 2): print(c)
