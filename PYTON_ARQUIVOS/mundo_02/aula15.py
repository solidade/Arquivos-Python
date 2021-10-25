# INTERROMPENDO REPETIÇÕES WHILE COM BREAK
b = 0
while True:
    print("I don't know!")
    b = b + 1
    if b == 20:
        break
print('Oh! I see!!')

s = c = 0
while True:
    n = int(input('Digite um valor qualquer: '))
    if n == 0:
        break
    s = s + n
    c = c + 1
#print('OK! Você digitou {} números e a soma deles equivale a {}'.format(c, s))
print(f'OK! Você digitou {c} números e a soma deles equivale a {s}')