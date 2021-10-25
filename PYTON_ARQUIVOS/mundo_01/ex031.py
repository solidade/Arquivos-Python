dist = int(input("Digite uma distância em KM e veja o custo da passagem: "))
if dist <= 200:
    print("O custo da passagem é de: R${}".format(dist * (1/2)))
else:
    print("O custo da passagem é de: R${}".format(dist * 0.45))

#  print(dist * 0.5 if dist<= 200 else dist * 0.45) assim também funciona
