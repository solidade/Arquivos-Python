s = float(input("Vamos calcular o valor do seu aumento? Digite o seu salário atual: R$ "))
if s > 1250:
    print("Você ganhou 10% de aumento. Seu novo salário é : R${}".format(s + (s / 100) * 10))
else:
    print("Você ganhou 15% de aumento. Seu novo salário é: R${}".format(s + (s / 100) * 15))

