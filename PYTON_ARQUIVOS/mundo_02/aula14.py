# ESTRUTURAS DE REPETIÇÃO
# LAÇO WHILE (significa 'enquanto')

# Um contador comum, vai contar até que a condição n < 10 seja falsa.
# n = 0
# while n < 10:
#    print(cont)
#    cont = cont + 1
# print('FIM')

# VAI SE REPETIR ENQUANTO A VARIÁVEL r = 'S'
# res = 'S'
# while res == 'S':
#    cont = int(input("Digite um valor aqui: "))
#    res = str(input("Deseja continuar [S / N]?: ")).upper()
# print("FIM")

# Contando pares e impares:
par = impar = 0
n = 1
print("PARA FINALIZAR OS VALORES DIGITADOS, DIGITE \033[31m0\033[m")
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Você digitou {} valores pares e {} valores impares.'.format(par, impar))