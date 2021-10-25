print('\033[31m=-=\033[m' * 17)
print('\033[33mSAIBA A SOMA DOS NUMEROS QUE DIGITAR [999 finaliza]\033[m')
print('\033[31m=-=\033[m' * 17)
s = c = 0
while True:
    n = int(input('Digite o valor que desejar: '))
    if n == 999:
        break
    s = s + n
    c = c + 1
print(f'OK! Você digitou {c} números e a soma deles equivale a {s}')