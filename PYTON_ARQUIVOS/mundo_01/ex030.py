num = int(input("Digite um número inteiro e descubra se ele é par ou impar: "))
n = num % 2
if n == 0:
    print("Você digitou {}, e ele é PAR".format(num))
else:
    print("Você digitou {}, e ele é IMPAR".format(num))
