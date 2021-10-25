# DEFININAOD O CABEÇALHO
print("\033[1:35m-=-\033[m" * 13)
print("\033[1:31mCALCULE A SUA MÉDIA E OBTENHA SEU RESULTADO")
print("\033[1:35m-=-\033[m" * 13)
# INPUTS DAS NOTAS DOS ALUNOS
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2
print("Sua média é {:.2f}".format(media))
# ESTRUTURAS LOGICAS CONDICIONAIS
if media >= 7:
    print("Muito Bem! Você foi APROVADO!")
elif 5 <= media < 7:
    print("Estude mais! Você precisará fazer RECUPERAÇÃO!")
else:
    print("Sinto muito! Você foi REPROVADO! Estude mais!")