import datetime
# DEFININAOD O CABEÇALHO
print("\033[1:35m-=-\033[m" * 13)
print("\033[1:31mVERIFIQUE O SEU PRAZO DE ALISTAMENTO MILITAR")
print("\033[1:35m-=-\033[m" * 13)
# DEFININDO O ANO ATUAL
date = datetime.datetime.today()
year = int(date.strftime('%Y'))
# FAZENDO OS INPUTS DOS ANOS DE NASCIMENTO DOS USUÀRIOS
ano = int(input("Digite o ano em que você nasceu: "))
# EXTRUTURAS LOGICAS CONDICIONAIS
if ano == year - 18:
    print("CHEGOU SUA VEZ DE SE ALISTAR! CORRA PARA UMAS DAS JUNTAS MILITARES O MAIS BREVE POSSIVEL.")
elif ano > year - 18:
    print("AINDA NÂO CHEGOU SUA VEZ! FALTAM {} ANOS PARA O SEU ALISTAMENTO".format(18 - (year - ano)))
else:
    print("VOCÊ ESTÀ ATRASADO! SEU PERIODO DE ALISTAMENTO PASSOU FAZ {} ANOS".format(year - 18 - ano))