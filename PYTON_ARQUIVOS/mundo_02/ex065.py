# Variáveis com códigos de cores!
vermelho, amarelo, azul1, lilas, azul, fim = '\033[1:31m', '\033[1:33m', '\033[1:34m', '\033[1:35m', \
                                             '\033[1:36m', '\033[m'
# ENTREGANDO DADOS SOBRE UM CONJUNTO DE NÚMEROS DIGITADOS

# Cabeçalho
print('\033[1:31m-=-\033[m' * 17)
print('\033[1:35mDIGITE QUANTOS NÚMEROS DESEJAR E OBTENHA DADOS DELES\033[m')
print('\033[1:31m-=-\033[m' * 17)
c = 0
s = 0
num = 0
maior = menor = 0


while num == 0:
    num = int(input('Digite o {}º número: '.format(c + 1)))
    prosseguir = int(input('\033[33mDeseja continuar?\033[m\n \033[36mSim [1]\n Não [2]\033[m\nSua escolha: '))
    c = c + 1
    s = s + num
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    if prosseguir == 1:
        num = 0
    elif prosseguir == 2:
        media = s / c
        print('\033[35mVocê digitou um total de\033[m \033[33m{}\033[m \033[35mnúmeros\033[m'.format(c))
        print('\033[35mA soma dos números digitado equivale a\033[m: \033[33m{}\033[m'.format(s))
        print('\033[35mA média dos números equivale a\033[m: \033[33m{}\033[m'.format(media))
        print('\033[35mO maior número digitado foi\033[m \033[33m{}\033[m \033[35me o menor foi '
              '\033[33m{}\033[m'.format(maior, menor))
    else:
        print('\033[31mOpção inválida! Tente novamente!\033[m')