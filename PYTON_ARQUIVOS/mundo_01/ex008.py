m = float(input("Digite um valor me metros "))
cm = m*100
mm = m*1000
print("{} metros é igual a {:.0f}dm, {:.0f}cm, ou {:.0f}mm".format(m, m*10, cm, mm))
print("Pode ser também {:.2f}dm, {:.2f}hm, ou {:.2f}km".format(m/10, m/100, m/100))

