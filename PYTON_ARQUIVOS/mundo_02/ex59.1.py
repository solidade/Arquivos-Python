# Variáveis com códigos de cores!
vermelho, amarelo, azul1, lilas, azul, fim = '\033[1:31m', '\033[1:33m', '\033[1:34m', '\033[1:35m', \
                                             '\033[1:36m', '\033[m'
# VERSÃO OFICIAL
from time import sleep
# Cabeçalho
print(vermelho, '-=-' * 9, fim)
print(azul, 'MOSTRANDO MENU DE OPÇÕES', azul)
print(vermelho, '-=-' * 9, fim)

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Finalizar o programa''')
    opcao = int(input('>>>>>>> Selecione uma opção: '))
    if opcao == 1:
        print('A soma entre {} e {} equivale a {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicação de {} e {} equivale a {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor entre {} e {} é: {}'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite um segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente outra vez!')
    print('=-=' * 10)
    sleep(3)
print('Você finalizou o programa! Volte sempre!')