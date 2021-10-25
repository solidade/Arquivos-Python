frase = str(input("Digite uma frase: ")).lower().strip()
print("Em sua frase, a letra 'a' aparece {} vezes".format(frase.count('a')))
print("A letra 'a' aparece pela primeira vez na posição {}".format(frase.find('a')))
print("A letra 'a' aparece a ultima vez na posição {}".format(frase.rfind('a')))

#  Pode adicionar +1 após frase.find('a') ou frase.rfind('a') para facilitar a contagem para o usuário
#  iniciando a contagem em 1 ao invés de 0