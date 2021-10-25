#  ANALISANDO CRÉDITO IMOBILIARIO
print('-=-' * 12)
print("AVALIANDO EMPRESTIMO IMOBILIARIO")
print('-=-' * 12)
casa = float(input("Qual o valor da casa que irá comprar? R$ "))
s = float(input("Quanto você ganha por mês? R$ "))
temp = float(input("Em quantos anos pretende pagar o empréstimo? "))
mes = temp * 12
par = casa / mes
if par > (s / 100) * 30:
    print("Sinto muito! Seu empréstimo imobiliário foi \033[1:31mRECUSADO\033[m.")
    print("O valor da parcela é superior a 30% de sua renda mensal.")
else:
    print("Parabéns! Seu empréstimo imobiliário foi \033[1:35mAPROVADO\033[m.")
    print("O valor de sua parcela será de R${:.2f}/mês por {:.0f}x".format(par, mes))