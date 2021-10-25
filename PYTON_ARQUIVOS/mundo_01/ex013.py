s = float(input("Digite o valor do seu salário: R$"))
a = (s/100)*15
print("Você ganhou um aumento de 15% no seu salário, o que equivale a R${:.2f}".format(a))
print("Seu novo salário, já com o aumento de 15%, é de R${:.2f}".format(s+a))
