# Variáveis com códigos de cores!
vermelho, amarelo, azul1, lilas, azul, fim = '\033[1:31m', '\033[1:33m', '\033[1:34m', '\033[1:35m', \
                                             '\033[1:36m', '\033[m'
# CONTANDO QUANTOS NÚMEROS FORAM DIGITADOS

# Cabeçalho
print('\033[1:31m-=-\033[m' * 15)
print('\033[1:35mDIGITE QUANTOS NÚMEROS DESEJAR E SAIBA A SOMA DELES\033[m')
print('\033[1:31m-=-\033[m' * 15)
c = 0
s = 0
num = 0

while num != 999:
    num = int(input('Digite o {}º número ou 999 para finalizar: '.format(c + 1)))
    c = c + 1
    s = s + num
    if num == 999:
        c = c - 1
        s = s - 999
        print('Você digitou {} números'.format(c))
        print('A soma dos números digitado equivale a: {}'.format(s))
