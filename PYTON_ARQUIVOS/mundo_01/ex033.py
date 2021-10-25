n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite um terceiro número: "))
if n1 > n2 > n3:
    print("Dentre os números digitados, {:.1f} é o menor e {:.1f} é o maior".format(n3, n1))
if n1 > n3 > n2:
    print("Dentre os números digitados, {:.1f} é o menor e {:.1f} é o maior".format(n2, n1))
if n2 > n1 > n3:
    print("Dentre os números digitados, {:.1f} é o menor e {:.1f} é o maior".format(n3, n2))
if n2 > n3 > n1:
    print("Dentre os números digitados, {:.1f} é o menor e {:.1f} é o maior".format(n1, n2))
if n3 > n1 > n2:
    print("Dentre os números digitados, {:.1f} é o menor e {:.1f} é o maior".format(n2, n3))
if n3 > n2 > n1:
    print("Dentre os números digitados, {:.1f} é o menor e {:.1f} é o maior".format(n1, n3))
