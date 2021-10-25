import random

# CABEÇALHO
print("\033[1:35m-=-\033[m" * 7)
print("\033[1:31mVAMOS JOGAR JOKENPÔ?")
print("\033[1:35m-=-\033[m" * 7)
# REGRAS DO JOGO
print("\033[2:30mREGRAS DO JOGO\033[m:\033[1:35m\n1. As regras serão iguais ao jogo original\n"
      "2. Você digitará sua jogada e eu farei a minha\n"
      "3. Exibirei na tela o vencedor\n"
      "4. Digite Pedra para pedra\n"
      "5. Digite Papel para papel\n"
      "6. Digite Tesoura para tesoura\n\033[m")
# VARIAVEL QUE ARMAZENARÀ O IMPUT E O RANDOM
player = str(input("Está pronto? Então pode fazer sua jogada: ")).title()
li = ["Pedra", "Papel", "Tesoura"]
pc = random.choice(li)
# ESTRUTURAS LOGICAS CONDICIONAIS
if player == pc:
    print("Você jogou {}\n"
          "Eu joguei {}\n"
          "EMPATAMOS!".format(player, pc))
elif (player == 'Pedra' and pc == 'Papel') or (player == 'Papel' and pc == 'Tesoura') or \
        (player == 'Tesoura' and pc == 'Pedra'):
    print("Você jogou {}\n"
          "Eu joguei {}\n"
          "EU GANHEI!".format(player, pc))
elif (pc == 'Pedra' and player == 'Papel') or (pc == 'Papel' and player == 'Tesoura') or \
        (pc == "Tesoura" and player == 'Pedra'):
    print("Você jogou {}\n"
          "Eu joguei {}\n"
          "Você ganhou! Parabéns!".format(player, pc))
else:
    print('Sua jogada é inválida. Verifique e tente novamente!')

# é possível criar uma lista de 0 a 2 para a escolha de pedra, papel ou tesoura.
# basicamente eu criaria duas variaveis com listas:
# uma com numeros de 0 a 2, vou chamar de computador
# e outra com os nomes pedra, papel e tesoura, irei chamar de itens
# a lista computador randomizada para a escolha do computador
# para fazer a referência é só usar .format(itens[computador])
# para o jogador, criaria a variável jogador para receber o input, e usaria .format(itens[jogador])
# Assim posso simplificar as escolhas do jogador usando numeros ao invés de palavras