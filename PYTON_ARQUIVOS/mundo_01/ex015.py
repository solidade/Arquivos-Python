km = float(input("Quantos Km você rodou com esse carro? "))
dias = int(input("Por quantos dias você alugou o carro? "))

print("Você alugou o carro por {} dias e rodou {:.0f}km com ele".format(dias, km))
print("{} dias equivale a R${:.2f}, e {:.0f}km equivale a R${:.2f}".format(dias, dias * 60, km, km * 0.15))
print("O valor total a ser pago é de R${}".format((dias * 60)+(km * 0.15)))
