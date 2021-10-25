import math
num = float(input("Digite um número real. ex: 76.378015. "))
print("O número {} tem a parte inteira {:.0f}".format(num, math.floor(num)))

#  print("O número {} tem a parte inteira {:.0f}".format(num, int(num)))
#  print("O número {} tem a parte inteira {:.0f}".format(num, math.trunc(num)))

#  Todas essas são formas de se fazer. Mas cuidado se apenas reduzir os números após o ponto, pois o número \n
#  pode ser arredondado para cima.