# Variáveis com códigos de cores!
vermelho, amarelo, azul1, lilas, azul, fim = '\033[1:31m', '\033[1:33m', '\033[1:34m', '\033[1:35m', \
                                             '\033[1:36m', '\033[m'
# CONSTRUINDO UMA PROGRESSÂO ARITIMETICA x2
import time

# Cabeçalho
print('\033[1:31m-=-\033[m' * 13)
print('\033[1:35mCONSTRUINDO UMA PROGRESSÂO ARITIMETICA x2\033[m')
print('\033[1:31m-=-\033[m' * 13)
# Variáveis
pt = int(input("\033[36mDigite o primeiro valor da PA: "))
r = int(input("\033[36mAgora digite a razão da PA: "))
u = pt + (r * 10)
print("\033[1:31mOK! Vou te dar os 10 primeiros termos da sua PA:\033[m")
time.sleep(1)
# Estrutura de laço while
while pt < u - 1:
    print(pt)
    pt = pt + r
    if pt == u:
        nt = int(input('\033[36mDeseja saber mais termos desta PA?\n'
                       'Digite quantos de termos que deseja exibir ou 0 para finalizar:\033[m '))
        if nt == 0:
            print('\033[31mPrograma finalizado!')
            quit()
        else:
            print(pt)
            u = pt + r * nt
            pt = pt + r
print('FIM')
