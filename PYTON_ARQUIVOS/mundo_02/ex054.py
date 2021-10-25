# DESCOBRINDO QUANTAS PESSOAS JÀ SÃO MAIORES DE IDADE NUM IMPUT
# Cabeçalho
from datetime import date

print('\033[1:31m-=-\033[m' * 26)
print('\033[1:35mDIGITE O ANO DE NASCIMENTO DE 7 PESSOAS E SAIBA QUANTAS SÃO MAIORES DE IDADE\033[m')
print('\033[1:31m-=-\033[m' * 26)
# Laço
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input("Digite o ano de nascimento da {}ª pessoa: ".format(c)))
    i = atual - ano
    if i >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('Dentre as pessoas que você escolheu, {} são maiores de idade e {} são menores de idade'.format(maior, menor))