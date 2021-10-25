import pygame

pygame.init()
pygame.mixer.music.load('vmm.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input("Curte essa melodia!")

#  import os, time
#  os.startfile(r'vmm.mp3')
#  time.sleep(10) 
#  Esse é outro método, mas vai abrir um reprodutor de audio disponível no pc
