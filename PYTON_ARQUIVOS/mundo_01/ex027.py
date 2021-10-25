nome = str(input("Digita seu nome completo: ")).split()
print("Olá, muito prazer em te conhecer!")
print("Seu primeiro nome é: {}".format(nome[0]))
print("Seu ultimo nome é: {}".format(nome[len(nome) - 1]))

#  posso utilizar o strip() no final do input para remover possíveis espaços que o usuário
#  use no inicio ou final do nome. Mas precisarei criar uma nova variável que receberá nome.split()
