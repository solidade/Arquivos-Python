from random import choice
# Variáveis com códigos de cores!
vermelho, amarelo, azul1, lilas, azul, fim = '\033[1:31m', '\033[1:33m', '\033[1:34m', '\033[1:35m', \
                                             '\033[1:36m', '\033[m'
# Cabeçalho
print(vermelho, '-=-' * 16, fim)
print(azul, 'ADVINHE O NÚMERO QUE ESTOU PENSANDO ENTRE 0 E 10', azul)
print(vermelho, '-=-' * 16, fim)
# vARIÁVEIS
jogador = int(input("Faça sua jogada: "))
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Poderia usar o randint(0, 10) ao invés da lista
computador = choice(list)  # não usaria o choice(list), usaria do randint(0, 10)
t = 0
# wHILE
while jogador != computador:
    print('Joguei {}'.format(computador))
    jogador = int(input("Você errou!\nFaça sua jogada: "))
    computador = choice(list)
    t = t + 1
print('Você acertou! Foram necesárias {} tentativas para o acerto.'.format(t + 1))
