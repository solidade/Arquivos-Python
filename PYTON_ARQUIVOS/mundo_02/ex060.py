# Variáveis com códigos de cores!
vermelho, amarelo, azul1, lilas, azul, fim = '\033[1:31m', '\033[1:33m', '\033[1:34m', '\033[1:35m', \
                                             '\033[1:36m', '\033[m'
# Cabeçalho
print(vermelho, '-=-' * 10, fim)
print(azul, 'TIRANDO O FATORIAL DE UM NÚMERO', azul)
print(vermelho, '-=-' * 10, fim)
# Variáveis
n = int(input("Digite um númeor de sua escolha: "))
cont = 1
nfix = n
tex = '\033[36m{}!\033[m = \033[35m{}'.format(n, n)
while n > 1:
    cont = cont * n  # Isso dá o valor final do fatorial, mas poderia apenas inportar o Factorial da biblioteca math
    n = n - 1
    tex = tex + '\033[35m x ' + str(n)
print(tex + ' = \033[33m{}\033[m'.format(cont))
print('\033[36m{}!\033[m = \033[33m{}\033[m'.format(nfix, cont))

#f, i = 1, 2   # DESSE MODO AQUI, NÃO MOSTRA O ESQUEMA, MOSTRA APENAS O VALOR FINAL DO FATORIAL
#while i <= n:
#    f = f * i
#    i = i + 1
#print('O valor de {}! = {}'.format(n, f))
