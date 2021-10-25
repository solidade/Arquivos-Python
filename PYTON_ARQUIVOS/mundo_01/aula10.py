rs = str(input("Você prefere Facebook, Instagram, Whatsapp ou Telegram? ")).title()
if rs == 'Telegram':
    print("Que legal! Telegram é uma excelente rede social")
if rs == 'Whatsapp':
    print("Whatsapp é uma rede super versátil e prática")
if rs == 'Instagram':
    print("Uau! Eu também! Tem cada página incrível por lá!")
if rs == 'Facebook':
    print("Legal! Utilizei o Facebook por muitos anos!")

#  É possível escrever de forma simplificada: print("Que legal!" if 'Telegram' else "Não gosto!")
#  if rs !== 'Telegram', 'Instagram', 'Whatsapp', "Facebook":
   #   print("Desculpe, não consegui compreender sua resposta")
