print('-=-' * 20)
print("ANALISADOR DE TRIANGULOS - DIGITE O COMPRIMENTO DE TRÊS RETAS")
print('-=-' * 20)

r1 = float(input("Digite o valor da primeira reta: "))
r2 = float(input("Digite o valor da segunda reta: "))
r3 = float(input("Digite o valor da terceira reta: "))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 +r2:
    print("As retas acima PODEM formar um trinângulo!")
else:
    print("Os seguimentos acima NÃO PODEM formar um triângulo")