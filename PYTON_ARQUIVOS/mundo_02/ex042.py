# CABEÇALHO
print("\033[1:35m-=-\033[m" * 20)
print("\033[1:31mANALISADOR DE TRIANGULOS - DIGITE O COMPRIMENTO DE TRÊS RETAS")
print("\033[1:35m-=-\033[m" * 20)
# VARIÀVEIS COM INPUTS DOS USUÀRIOS
r1 = float(input("Digite o valor da primeira reta: "))
r2 = float(input("Digite o valor da segunda reta: "))
r3 = float(input("Digite o valor da terceira reta: "))
#ESTRUTURAS LOGICAS CONDICIONAIS
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 +r2:
    if r1 == r2 == r3:
        print("As retas acima PODEM formar um triângulo EQUILÁTERO!")
    elif r1 != r2 != r3 != r1:
        print("As retas acima PODEM formar um triângulo ESCALENO!")
    else:
        print("As retas acima PODEM formar um triângulo ISÓSCELES")
else:
    print("Os seguimentos acima NÃO PODEM formar um triângulo!")