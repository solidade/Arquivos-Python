ano = int(input("Digite um ano e descubra se ele é bissexto: "))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("O ano {} é bissexto!".format(ano))
else:
    print("O ano {} NÃO é bissexto!".format(ano))
