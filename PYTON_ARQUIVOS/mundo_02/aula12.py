#  CONDICIONAIS ANINHADAS
print('-=-' * 13)
print("QUAL O SEU ANIME FAVORITO?\nNARUTO, ONE PIECE, BLEACH, DEATH NOTE")
print('-=-' * 13)
anime = str(input("Qual desses animes é o seu preferido? ")).upper()
if anime == 'NARUTO':
    print("Que legal! {} é excelente. Só não gostei muito do final.".format(anime))
elif anime == "BLEACH":
    print("Tamo junto! {} foi um dos melhores animes que já vi. É uma pena que cancelaram o anime!".format(anime))
elif anime == 'DEATH NOTE':
    print('Entre os animes curtos, {} é definitivamente o melhor!'.format(anime))
elif anime == "ONE PIECE":
    print('CARALHOOOOO! {} é o melhor anime que já foi produzido em todos os tempos! ODA é foda!'.format(anime))
else:
    print("Não conheço esse anime. Irei assistir para conferir se é bom mesmo!")