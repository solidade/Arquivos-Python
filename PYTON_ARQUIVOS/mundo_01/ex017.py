import math
co = float(input("Insira um valor para o comprimento do cateto oposto: "))
ca = float(input("Agora insira um valor para o comprimento do cateto ajacente: "))
print("A hipotenusa é {:.2f}".format(math.hypot(co, ca)))

## hipo = math.sqrt(co**2 + ca**2)
## print(hipo)
# Essa é outra possibilidade de se fazer
# Caso eu não quisesse importar nenhua biblioteca, poderia usar: hipo = (co**2 + ca**2) ** (1/2)

