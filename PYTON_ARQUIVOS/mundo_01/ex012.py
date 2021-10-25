p = float(input("Digite o preço orginal do produto: R$"))
d = (p/100)*5
print("Você ganhou 5% de desconto, que equivale R${:.2f}".format(d))
print("Seu produto com o desconto custará apenas R${:.2f}".format(p-d))
