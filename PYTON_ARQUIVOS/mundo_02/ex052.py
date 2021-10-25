# DESCOBRINDO NUMEROS PRIMOS
import time
# Cabeçalho
print('\033[1:31m-=-\033[m' * 9)
print('\033[1:35mDESCOBRINDO NUMEROS PRIMOS\033[m')
print('\033[1:31m-=-\033[m' * 9)

# Variáveis
num = int(input("Digite o número inteiro que deseja analisar: "))
print('\033[1:35mANALISANDO...\033[m')
time.sleep(2)

# FUNCIONA, MAS PROVAVELMENTE PODE SER SIMPLIFICADO
if num == 2 or num == 3 or num == 5 or num == 7:
    print("O número {} é um número PRIMO".format(num))
elif num != 1 and num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
    print("O número {} é um número PRIMO".format(num))
else:
    print("O número {} NÃO é um número PRIMO".format(num))

# SIMPLIFICANDO O CODIGO:
# CRiar mais uma variável, vou chamar ela de total e atribuir 0 a ela.
# for c in range(1, num + 1)
#   if num % c == 0:
#       print('\033[33m', end='')
#       total = total + 1
#   else:
#       print('\033[31m', end='')
#   print('{} '.format(c), end='')
# print('\n\033[mO número {} foi divisível {} vezes'.format(num, total)
# if total == 2:
#   print('E por isso ele é primo')
# else:
#   print('E por isso ele NÃO é primo')