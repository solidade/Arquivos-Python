#  ADICIONANDO CORES AO TERMINAL

#  \033[style;text;back]   essa é a ordem
#  \033[0;33;44m]   essa é a representação
#  os style são : 0 (sem stylo), 1 (negrito), 4 (sublinhado) e 7 (invertido texto/fundo)
#  as cores text são de 30 até 37 // ordem: branco, vermelho, verde, amarelo, azul, roxo, azul claro e cinza
#  as cores de fundo são de 40 até 47 // ordem: branco, vermelho, verde, amarelo, azul, roxo, azul claro e cinza
print("\033[1;30;43mOlá, Mundo!\033[m")
#  não é necessário mudar tudo, pode mudar só o stylo, ou só o texto ou só o fundo
#  VAMOS AO MELHOR MODO DE USAR
nome = 'Miqueias'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pb': '\033[7;30m'}
print("Olá! É um prazer conhecê-lo {}{}{}!!!".format(cores['azul'], nome, cores['limpa']))