# SOMANDO OS PARES dentre 6 números de INPUT
# Cabeçalho
print('\033[1:31m-=-\033[m' * 6)
print('\033[1:35mSOMANDO OS PARES\033[m')
print('\033[1:31m-=-\033[m' * 6)
print("\033[1:35mDIGITE 6 NÚMEROS INTEIROS MISTURANDO PARES E IMPARES\033[m")
# Estrutura de laço for
s = 0
cont = 0
for c in range(1, 7):
    n = int(input("Digite o {}º número: ".format(c)))
    if n % 2 == 0:
        cont = cont + 1
        s = s + n
print('Você digitou {} números pares, e a soma deles é: {}'.format(cont, s))
