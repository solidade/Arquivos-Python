# ADICIONANDO ITENS AO CARRINHO DE COMPRAS
from time import sleep
print('\033[31m=-=\033[m' * 13)
print('\033[33mADICIONANDO ITENS AO CARRINHO DE COMPRAS\033[m')
print('\033[31m=-=\033[m' * 13)
total = caro = barato = nome = c = 0
while True:
    item = str(input('Digite o nome do produto: '))
    valor = float(input('Qual o valor deste produto? R$'))
    print('---' * 10)
    continuar = str(input('Adicionar mais produtos? [S / N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Adicionar mais produtos? [S / N]: ')).upper().strip()[0]
    print('---' * 10)
    c = c + 1
    total = total + valor
    if valor > 1000:
        caro = caro + 1
    if c == 1:
        barato = valor
        nome = item
    else:
        if valor < barato:
            barato = valor
            nome = item
    if continuar == 'N':
        break
print('PROCESSANDO AS INFORMAÇÕES...')
sleep(4)
print(f'O valor total de sua compra é {total}')
print(f'{caro} dos produtos custam acima de R$1000')
print(f'{nome} é o produto mais barato da lista.')
