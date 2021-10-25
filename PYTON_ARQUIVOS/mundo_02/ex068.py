from random import randint
print('\033[31m=-=\033[m' * 7)
print('\033[33mJOGO DE PAR OU IMPAR\033[m')
print('\033[31m=-=\033[m' * 7)
c = 0
while True:
    num = int(input('Digite o valor que deseja jogar: '))
    jogador = str(input('Deseja PAR ou IMPAR [P / I]: ')).upper().strip()[0]
    while jogador not in 'PI':
        jogador = str(input('Deseja PAR ou IMPAR [P / I]: ')).upper().strip()[0]
    computer = randint(0, 10)
    soma = num + computer
    print('---' * 10)
    if soma % 2 != 0:
        print(f'Você jogou {num} e o computador {computer}. Total de {soma} DEU IMPAR')
        print('---' * 10)
        if jogador == 'I':
            c = c + 1
            print('Você VENCEU!\nVamos jogar novamente...')
            print('===' * 10)
        else:
            print('Você PERDEU!')
            break
    else:
        print(f'Você jogou {num} e o computador {computer}. Total de {soma} DEU PAR')
        print('---' * 10)
        if jogador == 'P':
            c = c + 1
            print('Você VENCEU!\nVamos jogar novamente...')
            print('===' * 10)
        else:
            print('Você PERDEU!')
            break
print('===' * 10)
print(f'GAME OVER! Você venceu {c} vezes.')