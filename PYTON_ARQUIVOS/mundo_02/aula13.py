# Estruturas de retições: laços, iterações
# LAÇO 'for' - Vai repetir um comando até que uma condição seja satisfeita

# Contagem de 0 até 10
# Note que o range indicado é até 11, mas será printado apenas até 10.
for number in range(0, 11):
    print(number)
print("FIM")

# Para contagem regressiva é necessário adicionar a iteração indicando que a contagem deve
# sempre reduzir o número em -1
# (note que o primeiro -1 é para que o contador atinja o 0, e o segundo é indicando a redução em -1)
for number in range(10, -1, -1):
    print(number)
print("FIM")

# É possível aumentar ou reduzir de 2 em 2 ou de 3 em 3, ou a qualquer taxa que desejar
# Basta mudar o valor da iteração para 2 ou -2, 3 ou -3, ou qualquer outro valor

# Somatório
s = 0
for number in range(0, 4):
    n = int(input("Digite um número: "))
    s = s + n
print("O somatório dos números é {}".format(s))