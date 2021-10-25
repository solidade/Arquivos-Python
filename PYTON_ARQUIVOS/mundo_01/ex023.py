num = int(input("Digite um número entre 0 e 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("O número digitado foi {}".format(num))
print("Unidade: {}". format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))
#  print("Unidade: {}".format(num[3]))
#  print("Dezena: {}".format(num[2]))
#  print("Centena: {}".format(num[1]))
#  print("Milhar: {}".format(num[0]))
#  Desse modo acima dá erro com números menores de 4 dígitos e com números flutuantes
