# CABEÇALHO
print("\033[1:35m-=-\033[m" * 10)
print("\033[1:31mCALCULANDO VALOR A SER PAGO")
print("\033[1:35m-=-\033[m" * 10)
# VARIAVEIS INPUTS
valor = float(input("Digite aqui o valor do produto que deseja comprar: R$"))
print("Confirmado o valor de R${} do seu produto!".format(valor))
f = int(input("Agora escolha a forma de pagamento:\n[1] Á vista (dinheiro ou cheque)\n"
              "[2] À vista no cartão de crédito\n"
              "[3] Até 2x no cartão\n"
              "[4] 3x ou mais no cartão\n"
              "Digite sua opção aqui: "))
# ESTRUTURAS CONDICIONAIS
if f == 1:
      print("Oba! Você ganhou 10% de desconto. O novo valor fica em: R${}".format(valor - (valor / 100 * 10)))
elif f == 2:
      print("Que legal! Você ganhou 5% de desconto. O novo valor fica em: R${}".format(valor - (valor / 100 * 5)))
elif f == 3:
      print("OK! Não há descontos nesta modalidade. Você pagará: R${}".format(valor))
elif f == 4:
      print("Há 20% de juros nesta modalidade! O novo valor fica em: R${}".format(valor + (valor / 100 * 20)))
else:
      print("Nenhuma opção selecionada. Verifique se digitou corratemente e tente novamente!")
