import random
nome1 = str(input("Insira o nome do primeiro aluno: "))
nome2 = str(input("Insira o nome do segundo aluno: "))
nome3 = str(input("Insira o nome do terceiro aluno: "))
nome4 = str(input("Insira o nome do quarto aluno: "))
print("O aluno sorteado foi {}".format(random.choice([nome1, nome2, nome3, nome4])))

# Caso haja a necessidade de repetição, utilizei os nome: Jhon, Jim, July e Joe
