a = int(input("Digite um número "))
b = a*2
c = a*3
d = a ** 0.5
print("O dobro de {} é {}, \no triplo é {} \ne a raiz quadrada é {:.2f}".format(a, b, c, d))

# outra possibilidade...:

a = int(input("Digite um número "))
print("O dobro de {} vale {}, \nO triplo vale {}, \nE a raiz quadrada vale {:.2f}".format(a, a*2, a*3, a**(1/2)))

# pode ser usado o parentese nas operações a*2, a*3 e a**(1/2)
# A raiz quadrada também pode ser obtida deste modo: pow(n, (1/2))
