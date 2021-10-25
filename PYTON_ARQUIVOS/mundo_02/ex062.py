# Variáveis com códigos de cores!
vermelho, amarelo, azul1, lilas, azul, fim = '\033[1:31m', '\033[1:33m', '\033[1:34m', '\033[1:35m', \
                                             '\033[1:36m', '\033[m'
# CONSTRUINDO UMA PROGRESSÂO ARITIMETICA x3
import time

# Cabeçalho
print('\033[1:31m-=-\033[m' * 13)
print('\033[1:35mCONSTRUINDO UMA PROGRESSÂO ARITIMETICA x3\033[m')
print('\033[1:31m-=-\033[m' * 13)
# Variáveis
pt = int(input("Digite o primeiro valor da PA: "))
r = int(input("Agora digite a razão da PA: "))
nt = int(input('Digite a quantidade de termos que deseja desta PA: '))
u = pt + (r * nt)
print("\033[1:31mOK! Vou te dar os {} primeiros termos da sua PA:\033[m".format(nt))
time.sleep(1)
# Estrutura de laço while
while pt < u - 1:
    print('{} --> '.format(pt), end='')
    pt = pt + r
print('FIM')