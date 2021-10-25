km = int(input("Há quantos km/h você está seu carro agora? "))
multa = (km - 80) * 7
if km > 80:
    print("Você foi multado! O limite de velocidade da estrada é 80Km/h")
    print("Você irá pagar R$7,00 por cada Km acima do limite.")
    print("Você está {}Km acima do limite e irá pagar R${} de multa".format(km - 80, multa))
else:
    print("Você está dentro do limite de velocidade. Siga em frente!")

#  Nesse caso o else não é obrigatório, bastaria identar o ultimo print para o canto esquerdo e o python entenderia
