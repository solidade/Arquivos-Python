cidade = str(input("Digite o nome de uma cidade: ")).strip()
print("Essa cidade comça com a palavra 'Santo'?")
print("Resposta: {}".format("Santo" in cidade[0:5].capitalize()))
