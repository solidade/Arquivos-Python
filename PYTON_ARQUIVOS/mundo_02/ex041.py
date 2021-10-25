import datetime

# DEFININAOD O CABEÇALHO
print("\033[1:35m-=-\033[m" * 12)
print("\033[1:31mSAIBA SUA CATEGORIA DE NATAÇÃO")
print("\033[1:35m-=-\033[m" * 12)
# IDENTIFICANDO O ANO ATUAL
date = datetime.datetime.today()
year = int(date.strftime('%Y'))
# INPUTS DAS IDADES DOS USUÁRIOS
ano = int(input("Digite o ano em que você nasceu: "))
idade = year - ano
# ESTRUTURAS LOGICAS CONDICIONAIS
if idade <= 9:
    print("Sua categoria de natação é \033[1:31mMIRIM\033[m")
elif 9 < idade <= 14:
    print("Sua categoria de natação é \033[1:31mINFANTIL\033[m")
elif 14 < idade <= 19:
    print("Sua categoria de natação é \033[1:31mJUNIOR\033[m")
elif 19 < idade <= 25:
    print("Sua categoria de natação é \033[1:31mSÊNIOR\033[m")
elif 25 < idade <= 120:
    print("Sua categoria de natação é \033[1:31mMASTER\033[m")
else:
    print("Desculpe, você já deve estar \033[1:31mMORTO\033[m!")

