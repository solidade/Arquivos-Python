# TESTE SE SUA FRASE È UM PALINDROMO
from unidecode import unidecode
# Cabeçalho
print('\033[1:31m-=-\033[m' * 11)
print('\033[1:35mTESTE SE SUA FRASE È UM PALINDROMO\033[m')
print('\033[1:31m-=-\033[m' * 11)
# VARIAVEIS E CONDICIONAIS
frase = str(input("Digite a frase que deseja analisar: ")).lower().strip()  # deixa td minúscula e remove spaces inuteis
f = unidecode(frase.replace(' ', ''))  # unidecode remove acentos da string, replace remove espaços no meio da frase
print("\033[1:35mVAMOS REMOVER OS ESPAÇOS DA SUA FRASE. OK?\033[m")
print("A frase sem os espaços fica assim: {}".format(f))
print('A frase invertida fica assim: {}'.format(f[::-1]))  # a informação nos colchetes serve para inverter a frase
if f == f[::-1]:
    print("\033[1:35mQue legal! A esta frase é um palindromo!\033[m")
else:
    print("\033[1:31mEsta frase não é um palindromo. Tente outra!\033[m")