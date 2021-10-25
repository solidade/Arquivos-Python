#Cabeçalho
print('\033[1:31m-=-\033[m' * 22)
print('\033[1:35mDIGITE O PESO (KG) DE 5 PESSOAS E SAIBA QUEM É A BALEIA E O PALITO\033[m')
print('\033[1:31m-=-\033[m' * 22)

# LAÇO
p = 0
b = 0
for c in range(1, 6):
    peso = float(input("Digite aqui o peso da {}ª pessoa: ".format(c)))
    if c == 1:
        p = peso
        b = peso
    else:
        if peso > b:
            b = peso
        if peso < p:
            p = peso
print("Dentre as pessoas que escolheu, a Baleia pesa {}Kg e o Palito pesa {}Kg".format(b, p))
