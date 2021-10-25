# CABEÇALHO
print("\033[1:35m-=-\033[m" * 7)
print("\033[1:31mCALCULANDO O SEU IMC")
print("\033[1:35m-=-\033[m" * 7)
# VARIAVEIS PARA ARMAZENAR VALORES DE INPUT DOS USUARIOS
peso = float(input("Digite o valor que você pesa em Kg: "))
altura = float(input("Digite o valor da sua altura em metros: "))
imc = peso / altura**2
# ESTRUTURAS LOGICAS CONDICIONAIS
print("IMC IDEAL: O IMC entre ideal é 18.5 e 25.")
if 18.5 <= imc < 25:
    print("Sue IMC é {:.1f}, seu peso está ideal!".format(imc))
elif imc < 18.5:
    print("Seu IMC é {:.1f}, você está abaixo do peso!".format(imc))
elif 25 <= imc < 30:
    print("Seu IMC é {:.1f}, você está com sobrepeso!".format(imc))
elif 30 <= imc < 40:
    print("Seu IMC é {:.1f}, você está obeso!".format(imc))
else:
    print("Seu IMC é {:.1f}, você está com obesidade morbida!".format(imc))
