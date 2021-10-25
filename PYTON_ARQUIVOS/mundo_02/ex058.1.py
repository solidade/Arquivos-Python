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
while jogador != computador:  # Há outras formas de se fazer, poderia criar uma variável chamada 'acertou' fora do laço
    if jogador < computador:  # Atribuiria 'False' para ela, e faria o laço assim: while not acertou: ...
        print('Mais... tente outra vez')  # colocaria o imput da variável 'jogador', e a somagem de 't'.
        jogador = int(input("Faça sua jogada: "))  # adicionaria um if jogador == computador: acertou = True
    if jogador > computador:
        print('Menos... tente outra vez')  # else: adicionaria if para verificar se o palpite foi maior ou menor
        jogador = int(input("Faça sua jogada: "))  # que o valor pensado pelo computador e, fora do laço, adicionaria
    t = t + 1  # o print final informando que acetou e a quantidade de tentativas
print('Você acertou! Foram necesárias {} tentativas para o acerto.'.format(t + 1))