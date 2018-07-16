import time
import pygame

def creditos(lista):
  for i in lista:
    time.sleep(1)
    print(lista[i])

lista = ["Desenvolvido por Ana Paula Lima, Isabela Hélebe e Ana Karolynne", "Projeto de Introdução a Programação", "Ministrado por Eduardo Falcão"]
pygame.init()
pygame.mixer.music.load("chi.mp3")
pygame.mixer.music.play()
pygame.mixer.music.wait()
creditos(lista)