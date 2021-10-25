print('\033[31m=-=\033[m' * 19)
print('\033[31mTABUADA DE QUALQUER VALOR [Valores negativos finalizam]\033[m')
print('\033[31m=-=\033[m' * 19)
c = 0
n = int(input('Deseja a tabuada de qual valor? '))
print('===' * 10)
while True:
    if n < 0:
        break
    c = c + 1
    operacao = n * c
    print(f'{n} x {c} = {operacao}')
    if c > 9:
        c = 0
        print('===' * 10)
        n = int(input('Deseja a tabuada de qual valor? '))
        print('===' * 10)
print('Tabuada finalizada! Volte sempre!')

#ALTERNATIVA
#while True:
#    n = int(input('Deseja a tabuada de qual valor? ')
#    print('---' * 10)
#    if n <= 0:
#        break
#    for c in range(1, 11):
#        print(f'{c} x {n} = {c * n})
#    print('---' * 10)
#print('Tabuada Finalizada!')

