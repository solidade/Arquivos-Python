# Variáveis com códigos de cores!
vermelho, amarelo, azul1, lilas, azul, fim = '\033[1:31m', '\033[1:33m', '\033[1:34m', '\033[1:35m', \
                                             '\033[1:36m', '\033[m'
# ESSE FOI DIFÍCIL PRACARALHO!!!!!!!!!
# Cabeçalho
print(vermelho, '-=-' * 9, fim)
print(azul, 'MOSTRANDO MENU DE OPÇÕES', azul)
print(vermelho, '-=-' * 9, fim)
# VARIÁVEIS
c = 1
s = 0
mt = 1
maior = menor = 0
while c < 3:
    num = int(input('Digite o {}º número: '.format(c)))
    c = c + 1
    s = s + num
    mt = mt * num
    if c == 2:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    if c >= 3:
        menu = int(input(' [1] Soma\n [2] Multiplicação\n [3] Maior\n [4] Novos números\n '
                 '[5] Sair do programa\n Selecione uma opção: '))
        if menu == 1:
            print('Você escolheu somar os números. A soma vale {}\n '.format(s))
        elif menu == 2:
            print('Você escolheu multiplicar os números. A multiplicação vale: {}'.format(mt))
        elif menu == 3:
            print('Você escolheu saber o maior número. O maior número digitado foi {} e o menor foi {}'.format(maior, menor))
        elif menu == 4:
            c, s, mt, maior, menor = 1, 0, 1, 0, 0
        elif menu == 5:
            print('Você escolheu sair do programa!')
            quit()
        else:
            print('Opção inválida! Tente novamente.')