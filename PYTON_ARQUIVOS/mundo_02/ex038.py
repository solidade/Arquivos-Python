# VERIFICANDO MAIOR DE DOIS NUMEROS
    # Cabeça-lho inicial para melhorar a comprensão e visualização pelo usuário
print("\033[1:35m-=-\033[m" * 12)
print("\033[1:31mVERIFIQUE O MAIOR ENTRE DOIS NUMEROS")
print("\033[1:35m-=-\033[m" * 12)
    # Variáveis que armazenará os valores digitados pelo usuário
n1 = int(input("Primeiro digite um número inteiro: "))
n2 = int(input("Agora digite outro número inteiro: "))
    # Condicionais lógicos para decidir qual resultado printar na tela do usuário
if n1 > n2:
    print("O \033[1:31mPRIMEIRO\033[m número ({}) é \033[1:35mMAIOR\033[m".format(n1))
elif n1 < n2:
    print("O \033[1:31mSEGUNDO\033[m número ({}) é \033[1:35mMAIOR\033[m".format(n2))
else:
    print("Não existe número maior, os dois números são \033[1:35mIGUAIS\033[m")
