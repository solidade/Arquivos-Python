# Tabuada usando o for

# Cabeçalho
print('\033[1:31m-=-\033[m' * 2)
print('\033[1:35mTABUADA\033[m')
print('\033[1:31m-=-\033[m' * 2)

# Variáveis
n = int(input("Digite o número que deseja calcular: "))
print('-=-' * 3)

# Estrutura de laço 'for'
for c in range(1, 10):
    tb = n * c
    print('{} x {} = {}'.format(n, c, tb))
print('-=-' * 3)