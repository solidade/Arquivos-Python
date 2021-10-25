import random
import time

print('-=-' * 17)
print("VOU PENSAR EM UM NUMERO ENTRE 0 E 5, TENTE ADVINHAR")
print('-=-' * 17)
n1 = int(input("Digite o número que você pensou: "))
n2 = [0, 1, 2, 3, 4, 5]
r = random.choice(n2)
#  r = randint(0, 5) esse comando elimina a necessidade de criar a variável n2
print("PROCESSANDO...")
time.sleep(3)
print("O número sorteado foi: {}".format(r))
if n1 == r:
    print("Parabéns! Você acertou!")
else:
    print("Desculpe, você errou!")

