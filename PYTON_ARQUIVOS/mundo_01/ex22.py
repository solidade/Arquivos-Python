nome = str(input("Digite o seu nome completo: "))
print("Seu nome em maiúscula {}".format(nome.upper()))
print("Seu nome em minúscula {}".format(nome.lower()))
lista = nome.split()
print("Quantidade de caracteres do seu nome sem os espaços: {}".format(len(''.join(lista))))
print("Seu primeiro nome tem {} caracteres".format(len(lista[0])))

#  no primeiro print é possivel adicional um .strip() no final para eliminar os espaços antes e depois do nome
#  no ultimo print, ao invés do .join(lista), é possível fazer len(nome) - nome.count(' ')
#  caso eu não queira criar a variável lista, posso usar o nome.find(' '), assim ele vai localizar em que
#  posição está o primeiro espaço. Assim consigo contar quantas letras tem o primeiro nome.
