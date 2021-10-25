import math
an = float(input("Insira o valor de ângulo qualquer. ex: 45. "))
print("O seno do ângulo {}º é igual a {:.2f}".format(an, math.sin(math.radians(an))))
print("O cosseno do ângulo {}º é igual a {:.2f}".format(an, math.cos(math.radians(an))))
print("A tangente do ângulo {}º é igual a {:.2f}".format(an, math.tan(math.radians(an))))

#  Foi necessário converter o valor do angulo para radianos porque as funções sin, cos e tan se baseiam
#  em radianos e não no angulo
#  Poderia ser criada uma variável para cada valor, mas optei por não fazer assim.
#  Caso eu importe somente as funções ao invés de toda biblioteca, não preciso usar o "math." antes.
