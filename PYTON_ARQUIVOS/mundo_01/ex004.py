h = input("Digite algo: ")
print("O tipo primitivo de {} é {}".format(h, type(h)))

print("{} é alfabético? {}".format(h, h.isalpha()))  # Usando o .format
print("{} é numérico? {}".format(h, h.isnumeric()))  # Usando o .format
print("{} é alfanumérico? {}".format(h, h.isalnum()))  # Usando o .format
print(h, "é um valor decimal?", h.isdecimal())
print(h, "é um espaço?", h.isspace())
print(h, "está em maiúscula?", h.isupper())
print(h, "está em minúscula?", h.islower())
print(h, "mescla maiúscula e minúscula?", h.istitle())
