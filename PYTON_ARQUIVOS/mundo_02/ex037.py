# CONVERSOR DE SISTEMAS NUMÈRICOS
print('\033[1:35m-=-\033[m' * 12)
print("\033[1:31mCONVERSOR DE SISTEMAS NUMÉRICOS\033[m")
print('\033[1:35m-=-\033[m' * 12)
num = int(input("Digite o número inteiro que deseja converter: "))
sis = int(input("Agora me diga para qual base deseja converter: \n"
                "[1] Binário\n[2] Octal\n[3] Hexadecimal\nDIGITE SUA OPÇÃO: "))
if sis == 1:
    print("O número {} convertido para Binário corresponde à: {}".format(num, bin(num)[2:]))
elif sis == 2:
    print("O número {} convertido para Octal corresponde à: {}".format(num, oct(num)[2:]))
elif sis == 3:
    print("O número {} convertido para Hexadecimal corresponde à: {}".format(num, hex(num)[2:]))
else:
    print("Você digitou errado a base numérica. Tente novamente!")